from __future__ import annotations

import base64
import json
import re
from io import BytesIO
from pathlib import Path

import numpy as np
from PIL import Image

from .base import HomeHubFeature, RuntimeBridge
try:
    from server_components.language_detector import detect_document_locale, normalize_locale
except ModuleNotFoundError:
    from runtime.server_components.language_detector import detect_document_locale, normalize_locale


BLUEPRINT = {
    "name": "Document OCR",
    "goal": "Reads uploaded images, extracts structured text and amounts, and recommends what HomeHub should do next.",
}

_RAPID_OCR_ENGINE = None


class Feature(HomeHubFeature):
    feature_id = "document-ocr"
    feature_name = "Document OCR"
    version = "1.0.0"

    def get_rapidocr_engine(self):
        global _RAPID_OCR_ENGINE
        if _RAPID_OCR_ENGINE is not None:
            return _RAPID_OCR_ENGINE
        try:
            from rapidocr_onnxruntime import RapidOCR

            _RAPID_OCR_ENGINE = RapidOCR()
        except Exception:
            _RAPID_OCR_ENGINE = None
        return _RAPID_OCR_ENGINE

    def run_local_ocr(self, image_base64: str) -> dict:
        if not image_base64:
            return {}
        engine = self.get_rapidocr_engine()
        if engine is None:
            return {}
        try:
            image_bytes = base64.b64decode(image_base64)
            image = Image.open(BytesIO(image_bytes)).convert("RGB")
            array = np.array(image)
            result, _ = engine(array)
        except Exception:
            return {}
        if not result:
            return {}
        lines: list[str] = []
        for item in result:
            if not isinstance(item, list) or len(item) < 2:
                continue
            text = str(item[1] if isinstance(item[1], str) else item[1][0] if isinstance(item[1], list) and item[1] else "").strip()
            if text:
                lines.append(text)
        if not lines:
            return {}
        ocr_text = "\n".join(lines)
        merchant = lines[0]
        detected_date = ""
        for line in lines:
            if re.search(r"\d{4}[/-]\d{1,2}[/-]\d{1,2}", line) or re.search(r"\d{4}年\d{1,2}月\d{1,2}日", line):
                detected_date = line
                break
        payment_method = ""
        for line in lines:
            lowered = line.lower()
            if "wechatpay" in lowered or "mechatpay" in lowered:
                payment_method = "MeChatPay" if "mechatpay" in lowered else "WeChat Pay"
                break
            if "paypay" in lowered:
                payment_method = "PayPay"
                break
            if "alipay" in lowered:
                payment_method = "Alipay"
                break
            if "visa" in lowered:
                payment_method = "Visa"
                break
            if "mastercard" in lowered:
                payment_method = "Mastercard"
                break
            if "現金" in line or "cash" in lowered:
                payment_method = "Cash"
                break
        tax_amount = 0
        for line in lines:
            if any(token in line for token in ["税", "tax", "消費税"]):
                tax_amount = max(tax_amount, self.parse_amount(line))
        summary = lines[0] if lines else ""
        return {
            "summary": summary,
            "contentType": "receipt" if any(token in ocr_text for token in ["合計", "お買上", "現計", "税込", "税", "小計"]) else "document",
            "relevantFacts": lines[:20],
            "merchant": merchant,
            "detectedDate": detected_date,
            "paymentMethod": payment_method,
            "currency": "JPY" if any(token in ocr_text for token in ["円", "日元", "JPY", "¥"]) else "",
            "taxAmount": tax_amount,
            "ocrText": ocr_text,
            "provider": "rapidocr",
            "model": "rapidocr_onnxruntime",
        }

    def merge_analysis(self, primary: dict, fallback: dict) -> dict:
        merged = dict(fallback)
        for key, value in primary.items():
            if isinstance(value, list):
                merged[key] = value if value else merged.get(key, [])
            elif isinstance(value, (int, float)):
                merged[key] = value if value else merged.get(key, 0)
            else:
                merged[key] = value if str(value).strip() else merged.get(key, "")
        return merged

    def logs_path(self, runtime: RuntimeBridge) -> Path:
        path = runtime.root / "logs"
        path.mkdir(parents=True, exist_ok=True)
        return path / "document_ocr_debug.jsonl"

    def append_debug_log(
        self,
        runtime: RuntimeBridge,
        request: dict,
        local_ocr: dict,
        raw_model: dict,
        analysis: dict,
        receipt_total: int,
    ) -> None:
        try:
            entry = {
                "timestamp": runtime.now_iso(),
                "message": str(request.get("message", "")).strip(),
                "attachmentName": str((request.get("attachment", {}) or {}).get("name", "")).strip(),
                "localOcr": local_ocr,
                "modelAnalysis": raw_model if isinstance(raw_model, dict) else {},
                "finalAnalysis": analysis,
                "selectedTotal": receipt_total,
            }
            with self.logs_path(runtime).open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception:
            return

    def parse_amount(self, value) -> int:
        text = str(value or "").strip().replace(",", "")
        if not text:
            return 0
        digits_only = re.sub(r"\D", "", text)
        if len(digits_only) >= 8 and "¥" not in text and "円" not in text and "jpy" not in text.lower():
            return 0
        match = re.search(r"(\d+(?:\.\d+)?)", text)
        if not match:
            return 0
        try:
            return int(float(match.group(1)))
        except (TypeError, ValueError):
            return 0

    def extract_amount_candidates(self, text: str) -> list[int]:
        cleaned = str(text or "").strip()
        if not cleaned:
            return []
        lowered = cleaned.lower()
        if re.search(r"\d{4}年\d{1,2}月\d{1,2}日", cleaned):
            return []
        if re.search(r"\d{4}[/-]\d{1,2}[/-]\d{1,2}", cleaned):
            return []
        if re.search(r"\d{1,2}:\d{2}", cleaned):
            return []
        if any(token in lowered for token in ["登録番号", "登记号", "電話", "tel", "問い合わせ", "問合", "receipt no", "レシート番号", "取引番号", "transaction", "店舗番号", "税務署", "invoice no"]):
            return []
        if re.search(r"\d{2,4}-\d{2,4}-\d{3,4}", cleaned):
            return []
        if re.search(r"\bt\d{8,}\b", lowered):
            return []
        candidates: list[int] = []
        for match in re.finditer(r"(?:¥\s*|円\s*|jpy\s*)?(\d{1,6}(?:,\d{3})*)(?:\s*(?:円|日元|jpy))?", cleaned, flags=re.IGNORECASE):
            raw = match.group(1)
            amount = self.parse_amount(raw)
            if amount <= 0:
                continue
            raw_digits = re.sub(r"\D", "", raw)
            has_currency_marker = any(token in lowered for token in ["¥", "円", "jpy", "日元"])
            has_total_marker = any(token in cleaned for token in ["合計", "総合計", "お買上", "お買い上げ", "現計", "請求額", "支払額", "利用額", "小計"])
            if len(raw_digits) >= 6 and not has_currency_marker and not has_total_marker:
                continue
            candidates.append(amount)
        return candidates

    def pick_receipt_total(self, analysis: dict) -> int:
        direct_candidates = [
            analysis.get("totalAmount", ""),
            analysis.get("subtotal", ""),
        ]
        for candidate in direct_candidates:
            amount = self.parse_amount(candidate)
            if amount > 0:
                return amount
        lines: list[str] = []
        for key in ["ocrText", "summary"]:
            raw = str(analysis.get(key, "")).strip()
            if raw:
                lines.extend(raw.splitlines())
        facts = analysis.get("relevantFacts", [])
        if isinstance(facts, list):
            lines.extend(str(item).strip() for item in facts if str(item).strip())
        weighted: list[tuple[int, int]] = []
        for line in lines:
            cleaned = str(line).strip()
            if not cleaned:
                continue
            lowered = cleaned.lower()
            amounts = self.extract_amount_candidates(cleaned)
            if not amounts:
                continue
            for amount in amounts:
                score = 1
                if any(token in cleaned for token in ["¥", "￥", "円", "JPY", "日元"]):
                    score = 4
                if any(token in cleaned for token in ["合計", "総合計", "お買上", "お買い上げ", "現計", "請求額", "支払額", "利用額", "收款", "收据", "收银"]):
                    score = 6
                elif any(token in cleaned for token in ["小計", "subtotal"]):
                    score = 4
                elif any(token in cleaned for token in ["税", "tax", "内消費税"]):
                    score = 2
                elif "mechatpay" in lowered or "wechatpay" in lowered or "paypay" in lowered:
                    score = 5
                if re.search(r"\d{4}年\d{1,2}月\d{1,2}日", cleaned) or re.search(r"\d{4}[/-]\d{1,2}[/-]\d{1,2}", cleaned):
                    score = -1
                if amount >= 1000000:
                    score = -1
                weighted.append((score, amount))
        if not weighted:
            return 0
        weighted.sort(key=lambda item: (item[0], item[1]), reverse=True)
        for score, amount in weighted:
            if amount >= 100000 and score < 4:
                continue
            if score > 0:
                return amount
        return 0

    def find_first_line_value(self, analysis: dict, patterns: list[str]) -> str:
        lines: list[str] = []
        for key in ["ocrText", "summary"]:
            raw = str(analysis.get(key, "")).strip()
            if raw:
                lines.extend(raw.splitlines())
        facts = analysis.get("relevantFacts", [])
        if isinstance(facts, list):
            lines.extend(str(item).strip() for item in facts if str(item).strip())
        for line in lines:
            cleaned = str(line).strip()
            lowered = cleaned.lower()
            if any(pattern in lowered for pattern in patterns):
                return cleaned
        return ""

    def detect_payment_method(self, analysis: dict) -> str:
        direct = str(analysis.get("paymentMethod", "")).strip()
        if direct:
            return direct
        line = self.find_first_line_value(analysis, ["wechatpay", "mechatpay", "visa", "mastercard", "cash", "現金", "カード", "paypay", "支付宝", "alipay"])
        if not line:
            return ""
        lowered = line.lower()
        if "mechatpay" in lowered:
            return "MeChatPay"
        if "wechatpay" in lowered:
            return "WeChat Pay"
        if "paypay" in lowered:
            return "PayPay"
        if "alipay" in lowered:
            return "Alipay"
        if "visa" in lowered:
            return "Visa"
        if "mastercard" in lowered:
            return "Mastercard"
        if "現金" in line or "cash" in lowered:
            return "Cash"
        if "カード" in line:
            return "Card"
        return line

    def detect_merchant(self, analysis: dict) -> str:
        direct = str(analysis.get("merchant", "")).strip()
        if direct:
            return direct
        ocr_text = str(analysis.get("ocrText", "")).strip()
        if ocr_text:
            first_line = next((line.strip() for line in ocr_text.splitlines() if line.strip()), "")
            if first_line:
                return first_line
        return ""

    def detect_date(self, analysis: dict) -> str:
        direct = str(analysis.get("detectedDate", "")).strip()
        if direct and not re.search(r"\d{2,4}-\d{2,4}-\d{3,4}", direct):
            return direct
        lines = []
        for key in ["ocrText", "summary"]:
            raw = str(analysis.get(key, "")).strip()
            if raw:
                lines.extend(raw.splitlines())
        for line in lines:
            cleaned = str(line).strip()
            if re.search(r"\d{4}年\d{1,2}月\d{1,2}日", cleaned):
                return cleaned
            if re.search(r"\d{4}[/-]\d{1,2}[/-]\d{1,2}", cleaned) and not re.search(r"\d{2,4}-\d{2,4}-\d{3,4}", cleaned):
                return cleaned
        return ""

    def descriptor(self) -> dict:
        data = super().descriptor()
        data["summary"] = BLUEPRINT["goal"]
        data["blueprint"] = BLUEPRINT
        return data

    def normalize_analysis(self, raw: dict) -> dict:
        analysis = dict(raw or {}) if isinstance(raw, dict) else {}
        relevant = analysis.get("relevantFacts", [])
        if not isinstance(relevant, list):
            relevant = [str(relevant)] if str(relevant).strip() else []
        normalized_expenses: list[dict] = []
        raw_expenses = analysis.get("detectedExpenses", [])
        if isinstance(raw_expenses, list):
            for item in raw_expenses:
                if not isinstance(item, dict):
                    continue
                try:
                    amount = int(float(item.get("amount", 0) or 0))
                except (TypeError, ValueError):
                    amount = 0
                if amount <= 0:
                    continue
                normalized_expenses.append({
                    "amount": amount,
                    "category": str(item.get("category", "")).strip(),
                    "content": str(item.get("content", "")).strip(),
                    "note": str(item.get("note", "")).strip(),
                })
        return {
            "summary": str(analysis.get("summary", "")).strip(),
            "contentType": str(analysis.get("contentType", "")).strip(),
            "relevantFacts": [str(item).strip() for item in relevant if str(item).strip()],
            "suggestedAction": str(analysis.get("suggestedAction", "")).strip(),
            "recommendedAction": str(analysis.get("recommendedAction", "")).strip() or ("record_expense" if normalized_expenses else ""),
            "followUpQuestion": str(analysis.get("followUpQuestion", "")).strip(),
            "confidence": float(analysis.get("confidence", 0) or 0),
            "requiresUserReview": bool(analysis.get("requiresUserReview", False)),
            "currency": str(analysis.get("currency", "")).strip(),
            "merchant": self.detect_merchant(analysis),
            "detectedDate": self.detect_date(analysis),
            "paymentMethod": self.detect_payment_method(analysis),
            "ocrText": str(analysis.get("ocrText", "")).strip(),
            "totalAmount": self.parse_amount(analysis.get("totalAmount", "")),
            "subtotal": self.parse_amount(analysis.get("subtotal", "")),
            "taxAmount": self.parse_amount(analysis.get("taxAmount", "")),
            "documentLanguage": str(analysis.get("documentLanguage", "")).strip(),
            "detectedExpenses": normalized_expenses,
            "provider": str(analysis.get("provider", "")).strip(),
            "model": str(analysis.get("model", "")).strip(),
        }

    def build_analysis_prompt(self, payload: dict, locale: str, document_language: str = "") -> str:
        agent = payload.get("agent", {}) if isinstance(payload.get("agent"), dict) else {}
        profile = agent.get("profile", {}) if isinstance(agent.get("profile"), dict) else {}
        message = str(payload.get("message", "")).strip()
        language_hint = document_language or locale
        return (
            "You are HomeHub's OCR and document understanding feature. "
            "Read the uploaded image and return JSON only with keys: "
            "summary, contentType, relevantFacts, suggestedAction, recommendedAction, followUpQuestion, confidence, requiresUserReview, "
            "currency, merchant, detectedDate, paymentMethod, totalAmount, subtotal, taxAmount, ocrText, documentLanguage, detectedExpenses. "
            "Use relevantFacts as an array of short strings. "
            "Use detectedExpenses as an array of objects with keys amount, category, content, note. "
            "recommendedAction must be one of: record_expense, extract_text_only, ask_follow_up, no_action. "
            "The interface language and the document language may be different. Always interpret the receipt in its original language first, then answer in the user locale. "
            "If the receipt text is Japanese, use Japanese receipt conventions such as 合計, 現計, お買上, 小計, 内消費税, 税込, ご利用額, 点, and レシート番号. "
            "If the user's language or the agent context implies adding this image into a bill, expense, spending log, reimbursement log, or family ledger, "
            "set recommendedAction to record_expense and extract each visible expense amount that should be recorded. "
            "For retail receipts, prioritize the final payable total, for example lines like 合計, お買上, 現計, 支払額, 請求額, MeChatPay ご利用額, total, or amount due. "
            "When you can identify the final receipt total, fill totalAmount with that number and include one detectedExpenses item for that total even if line-item OCR is incomplete. "
            "ocrText should contain the most important OCR lines, especially merchant, date, total, tax, and payment lines. "
            "If no reliable amount is visible, return an empty detectedExpenses array and use ask_follow_up or no_action. "
            f"User message: {message}. "
            f"Agent name: {agent.get('name', '')}. "
            f"Agent goal: {profile.get('goal', '')}. "
            f"Expected inputs: {profile.get('inputs', '')}. "
            f"Expected output: {profile.get('output', '')}. "
            f"User locale: {locale}. "
            f"Document language hint: {language_hint}."
        )

    def run_feature(self, runtime: RuntimeBridge, source: str, payload: dict | None = None) -> dict | None:
        request = dict(payload or {})
        action = str(request.get("action", "")).strip().lower() or "analyze_attachment"
        if action not in {"analyze_attachment", "ocr_scan"}:
            return {"ok": False, "error": f"Unsupported OCR action: {action}"}
        attachment = request.get("attachment", {}) if isinstance(request.get("attachment"), dict) else {}
        image_base64 = str(attachment.get("imageBase64", "")).strip()
        mime_type = str(attachment.get("mimeType", "image/png")).strip() or "image/png"
        locale = normalize_locale(str(request.get("locale", "zh-CN")), "zh-CN")
        if not image_base64:
            return {"ok": False, "error": "attachment_required", "reply": "No image attachment was provided."}
        if not runtime.analyze_image:
            return {"ok": False, "error": "ocr_runtime_unavailable", "reply": "OCR runtime is not available."}
        local_ocr = self.run_local_ocr(image_base64)
        document_language = detect_document_locale(local_ocr.get("ocrText", ""), locale)
        local_ocr["documentLanguage"] = document_language
        prompt = self.build_analysis_prompt(request, locale, document_language)
        if local_ocr.get("ocrText"):
            prompt += f" Local OCR text candidate:\n{local_ocr.get('ocrText', '')}\nUse it as a strong hint, especially for merchant, date, tax, payment method, and total."
        raw = runtime.analyze_image(prompt, image_base64, mime_type, "qwen2.5vl:7b") if runtime.analyze_image else None
        raw_dict = raw if isinstance(raw, dict) else {}
        merged_raw = self.merge_analysis(raw_dict, local_ocr)
        analysis = self.normalize_analysis(merged_raw)
        analysis["documentLanguage"] = analysis.get("documentLanguage") or document_language
        receipt_total = self.pick_receipt_total(analysis)
        if receipt_total > 0:
            analysis["totalAmount"] = receipt_total
        if not analysis["detectedExpenses"] and receipt_total > 0:
            analysis["detectedExpenses"] = [{
                "amount": receipt_total,
                "category": "餐饮" if any(token in str(analysis.get("summary", "")) for token in ["餐", "食", "lawson", "store"]) else "其他",
                "content": str(analysis.get("merchant", "")).strip() or "Receipt total",
                "note": str(analysis.get("detectedDate", "")).strip(),
                "merchant": str(analysis.get("merchant", "")).strip(),
                "purchaseDate": str(analysis.get("detectedDate", "")).strip(),
                "paymentMethod": str(analysis.get("paymentMethod", "")).strip(),
                "taxAmount": int(analysis.get("taxAmount", 0) or 0),
            }]
            analysis["recommendedAction"] = analysis.get("recommendedAction") or "record_expense"
        self.append_debug_log(runtime, request, local_ocr, raw_dict, analysis, receipt_total)
        if locale == "zh-CN":
            if analysis.get("totalAmount"):
                merchant = str(analysis.get("merchant", "")).strip()
                merchant_text = f" {merchant}" if merchant else ""
                reply = f"我已经识别这张票据了{merchant_text}，当前看到的总金额是 {int(analysis['totalAmount'])} 日元。"
            else:
                reply = analysis["summary"] or "我已经看过这张图片了。"
        else:
            if analysis.get("totalAmount"):
                merchant = str(analysis.get("merchant", "")).strip()
                merchant_text = f" at {merchant}" if merchant else ""
                reply = f"I reviewed the receipt{merchant_text}. The total I can see is {int(analysis['totalAmount'])} JPY."
            else:
                reply = analysis["summary"] or "I reviewed the uploaded image."
        return {"ok": True, "action": action, "analysis": analysis, "reply": reply}

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        return None


def load_feature() -> HomeHubFeature:
    return Feature()
