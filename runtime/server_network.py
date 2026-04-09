from __future__ import annotations

import json
import re
from urllib.parse import parse_qs, quote, unquote, urlencode, urlparse

try:
    import trafilatura
except ModuleNotFoundError:
    trafilatura = None


def normalize_domain(value):
    host = str(value or "").strip().lower()
    if not host:
        return ""
    if "://" in host:
        host = urlparse(host).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host.split(":")[0]


def domain_allowed(host, allowed_domains):
    normalized = normalize_domain(host)
    return any(normalized == item or normalized.endswith(f".{item}") for item in allowed_domains)


def extract_urls_from_text(text):
    return re.findall(r'https?://[^\s)>\"]+', str(text or ""))


def strip_html_excerpt(html_text, limit=420):
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", html_text)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    title_match = re.search(r"(?is)<title[^>]*>(.*?)</title>", text)
    title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", title_match.group(1))).strip() if title_match else ""
    meta_match = re.search(r'(?is)<meta[^>]+(?:name|property)=["\'](?:description|og:description|twitter:description)["\'][^>]+content=["\'](.*?)["\']', text)
    meta_description = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", meta_match.group(1))).strip() if meta_match else ""
    article_match = re.search(r"(?is)<article[^>]*>(.*?)</article>", text)
    article_plain = ""
    if article_match:
        article_plain = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", article_match.group(1))).strip()
    plain = re.sub(r"(?s)<[^>]+>", " ", text)
    plain = re.sub(r"\s+", " ", plain).strip()
    excerpt = article_plain or meta_description or plain
    return {"title": title, "excerpt": excerpt[:limit]}


def extract_best_excerpt(content, limit=420):
    if isinstance(content, dict):
        return json.dumps(content, ensure_ascii=False)[:limit]
    raw = str(content or "")
    if trafilatura is not None:
        try:
            extracted = trafilatura.extract(
                raw,
                include_comments=False,
                include_tables=False,
                favor_precision=True,
            )
            cleaned = re.sub(r"\s+", " ", str(extracted or "")).strip()
            if cleaned:
                return cleaned[:limit]
        except Exception:
            pass
    return strip_html_excerpt(raw, limit=limit).get("excerpt", "")


def clean_network_excerpt(text, limit=220):
    value = str(text or "").strip()
    if not value:
        return ""
    value = re.sub(r"https?://\S+", " ", value)
    value = re.sub(r"\b(?:www\.)?[a-z0-9.-]+\.[a-z]{2,}\S*", " ", value, flags=re.IGNORECASE)
    value = re.sub(r"\s+", " ", value).strip(" -:|;,\n\t")
    boilerplate_tokens = [
        "cookie",
        "privacy",
        "terms",
        "advertisement",
        "sign in",
        "log in",
        "javascript",
        "enable javascript",
        "版权所有",
        "隐私",
        "条款",
        "登录",
        "注册",
    ]
    pieces = re.split(r"(?<=[。！？.!?])\s+|[\n\r]+", value)
    filtered = []
    for piece in pieces:
        candidate = str(piece or "").strip(" -:|;,")
        lowered = candidate.lower()
        if len(candidate) < 8:
            continue
        if any(token in lowered for token in boilerplate_tokens):
            continue
        filtered.append(candidate)
    joined = " ".join(filtered) if filtered else value
    return joined[:limit].rstrip(" ,;:") + ("..." if len(joined) > limit else "")


def build_source_labels(sources):
    labels = []
    for item in sources[:3]:
        title = str(item.get("title", "")).strip()
        url = str(item.get("url", "")).strip()
        domain = normalize_domain(url)
        if title and domain:
            labels.append(f"{title} ({domain})")
        elif title:
            labels.append(title)
        elif domain:
            labels.append(domain)
        elif url:
            labels.append(url)
    return labels


def synthesize_network_answer(result, locale):
    sources = result.get("sources", [])
    cleaned_excerpts = []
    for item in sources[:3]:
        cleaned = clean_network_excerpt(item.get("excerpt", ""))
        if cleaned:
            cleaned_excerpts.append(cleaned)

    primary = cleaned_excerpts[0] if cleaned_excerpts else clean_network_excerpt(result.get("answer", ""))
    secondary = ""
    for item in cleaned_excerpts[1:]:
        if item and item != primary:
            secondary = item
            break

    if locale == "zh-CN":
        if primary and secondary:
            return f"我整理了一下联网结果：{primary} 另外，其他来源也提到：{secondary}"
        if primary:
            return f"我整理了一下联网结果：{primary}"
        return "我已经完成联网查询，但当前来源里没有提取到足够清晰的正文内容。"
    if locale == "ja-JP":
        if primary and secondary:
            return f"ネット検索結果を整理すると、{primary} 別の情報源では、{secondary}"
        if primary:
            return f"ネット検索結果を整理すると、{primary}"
        return "ネット検索は完了しましたが、情報源から十分に明確な本文を抽出できませんでした。"
    if primary and secondary:
        return f"Here is the cleaned-up result: {primary} Another source also notes: {secondary}"
    if primary:
        return f"Here is the cleaned-up result: {primary}"
    return "I completed the network lookup, but the fetched sources did not contain enough clean text to summarize clearly."


def fetch_allowed_url(url, allowed_domains, json_get):
    host = normalize_domain(url)
    if not domain_allowed(host, allowed_domains):
        return {"ok": False, "error": f"domain_not_allowed:{host}"}
    try:
        content = json_get(url, headers={"User-Agent": "HomeHub/0.1"})
    except Exception as exc:
        return {"ok": False, "error": f"fetch_failed:{exc}"}
    if isinstance(content, dict):
        return {"ok": True, "url": url, "title": str(content.get("title", "")).strip(), "excerpt": extract_best_excerpt(content)}
    parsed = strip_html_excerpt(str(content))
    excerpt = extract_best_excerpt(content)
    return {"ok": True, "url": url, "title": parsed.get("title", ""), "excerpt": excerpt or parsed.get("excerpt", "")}


def wikipedia_lookup(query, locale, json_get):
    language = "zh" if str(locale).startswith("zh") else ("ja" if str(locale).startswith("ja") else "en")
    params = urlencode({"action": "opensearch", "search": query, "limit": 1, "namespace": 0, "format": "json"})
    search_url = f"https://{language}.wikipedia.org/w/api.php?{params}"
    try:
        response = json_get(search_url, headers={"User-Agent": "HomeHub/0.1"})
    except Exception as exc:
        return {"ok": False, "error": f"wikipedia_search_failed:{exc}"}
    if not isinstance(response, list) or len(response) < 4 or not response[1]:
        return {"ok": False, "error": "no_wikipedia_match"}
    title = str(response[1][0]).strip()
    summary_url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"
    try:
        summary = json_get(summary_url, headers={"User-Agent": "HomeHub/0.1"})
    except Exception as exc:
        return {"ok": False, "error": f"wikipedia_summary_failed:{exc}"}
    if not isinstance(summary, dict):
        return {"ok": False, "error": "invalid_wikipedia_summary"}
    return {
        "ok": True,
        "url": str(summary.get("content_urls", {}).get("desktop", {}).get("page", "")).strip() or summary_url,
        "title": str(summary.get("title", title)).strip(),
        "excerpt": str(summary.get("extract", "")).strip(),
    }


def build_network_lookup_reply(result, locale):
    if not result.get("ok"):
        if locale == "zh-CN":
            return f"这次受控联网查询没有拿到结果：{result.get('error', 'unknown error')}。"
        if locale == "ja-JP":
            return f"制御付きネット検索は結果を返せませんでした: {result.get('error', 'unknown error')}."
        return f"The controlled network lookup did not return a usable result: {result.get('error', 'unknown error')}."
    answer = synthesize_network_answer(result, locale)
    sources = result.get("sources", [])
    source_labels = build_source_labels(sources)
    if locale == "zh-CN":
        if source_labels:
            return f"{answer}\n来源：{'；'.join(source_labels)}"
        return answer
    if source_labels:
        return f"{answer}\nSources: {'; '.join(source_labels)}"
    return answer


def perform_controlled_network_lookup(query, locale, policies, json_get, policy_id="safe-general", preferred_sources=None, allowed_domains=None):
    policy = policies.get(policy_id) or policies["safe-general"]
    merged_domains = [normalize_domain(item) for item in policy.get("allowedDomains", [])]
    for item in preferred_sources or []:
        normalized = normalize_domain(item)
        if normalized and "." in normalized and normalized not in merged_domains:
            merged_domains.append(normalized)
    for item in allowed_domains or []:
        normalized = normalize_domain(item)
        if normalized and normalized not in merged_domains:
            merged_domains.append(normalized)

    sources = []
    direct_urls = extract_urls_from_text(query)
    for url in direct_urls[: policy.get("maxSources", 3)]:
        fetched = fetch_allowed_url(url, merged_domains, json_get)
        if fetched.get("ok"):
            sources.append(fetched)
    if not sources and domain_allowed("wikipedia.org", merged_domains):
        wiki = wikipedia_lookup(query, locale, json_get)
        if wiki.get("ok"):
            sources.append(wiki)
    if not sources:
        return {
            "ok": False,
            "error": "no_allowed_source_found",
            "policy": policy["id"],
            "allowedDomains": merged_domains,
            "sources": [],
        }

    answer = sources[0].get("excerpt", "").strip()
    if len(answer) > 320:
        answer = answer[:320].rstrip() + "..."
    title = str(sources[0].get("title", "")).strip()
    if title:
        answer = f"{title}: {answer}" if answer else title
    return {
        "ok": True,
        "policy": policy["id"],
        "allowedDomains": merged_domains,
        "answer": answer,
        "sources": sources[: policy.get("maxSources", 3)],
    }


def is_private_or_local_host(host):
    normalized = normalize_domain(host)
    if not normalized:
        return True
    if normalized in {"localhost", "0.0.0.0"}:
        return True
    if normalized.startswith("127.") or normalized.startswith("10.") or normalized.startswith("192.168."):
        return True
    if normalized.startswith("172."):
        parts = normalized.split(".")
        if len(parts) >= 2:
            try:
                second = int(parts[1])
            except ValueError:
                second = -1
            if 16 <= second <= 31:
                return True
    return False


def fetch_discovered_url(url, json_get):
    parsed = urlparse(str(url or "").strip())
    if parsed.scheme not in {"https", "http"}:
        return {"ok": False, "error": "unsupported_scheme"}
    if is_private_or_local_host(parsed.netloc):
        return {"ok": False, "error": "private_or_local_host"}
    try:
        content = json_get(url, headers={"User-Agent": "HomeHub/0.1"}, timeout=20)
    except Exception as exc:
        return {"ok": False, "error": f"fetch_failed:{exc}"}
    if isinstance(content, dict):
        return {"ok": True, "url": url, "title": str(content.get("title", "")).strip(), "excerpt": extract_best_excerpt(content)}
    parsed_content = strip_html_excerpt(str(content))
    excerpt = extract_best_excerpt(content)
    return {"ok": True, "url": url, "title": parsed_content.get("title", ""), "excerpt": excerpt or parsed_content.get("excerpt", "")}


def discover_search_result_urls(query, json_get, max_results=5):
    search_query = str(query or "").strip()
    if not search_query:
        return []
    search_url = f"https://duckduckgo.com/html/?q={quote(search_query)}"
    try:
        html = str(json_get(search_url, headers={"User-Agent": "HomeHub/0.1"}, timeout=20))
    except Exception:
        return []
    urls = []
    seen = set()
    for match in re.findall(r'href="([^"]+)"', html):
        candidate = str(match or "").strip()
        if not candidate:
            continue
        if candidate.startswith("//duckduckgo.com/l/?"):
            candidate = f"https:{candidate}"
        parsed = urlparse(candidate)
        if "duckduckgo.com" in parsed.netloc:
            uddg = parse_qs(parsed.query).get("uddg", [])
            if uddg:
                candidate = unquote(str(uddg[0]).strip())
        final_parsed = urlparse(candidate)
        if final_parsed.scheme not in {"https", "http"}:
            continue
        host = normalize_domain(final_parsed.netloc)
        if not host or host in seen or is_private_or_local_host(host) or "duckduckgo.com" in host:
            continue
        seen.add(host)
        urls.append(candidate)
        if len(urls) >= max_results:
            break
    return urls


def perform_network_lookup(query, locale, policies, json_get, policy_id="official-only", preferred_sources=None, allowed_domains=None):
    controlled = perform_controlled_network_lookup(query, locale, policies, json_get, policy_id, preferred_sources, allowed_domains)
    if controlled.get("ok"):
        return controlled
    discovered_sources = []
    for url in discover_search_result_urls(query, json_get, max_results=3):
        fetched = fetch_discovered_url(url, json_get)
        if fetched.get("ok"):
            discovered_sources.append(fetched)
    if not discovered_sources:
        return controlled
    answer = discovered_sources[0].get("excerpt", "").strip()
    if len(answer) > 320:
        answer = answer[:320].rstrip() + "..."
    title = str(discovered_sources[0].get("title", "")).strip()
    if title:
        answer = f"{title}: {answer}" if answer else title
    return {
        "ok": True,
        "policy": policy_id or "official-only",
        "allowedDomains": allowed_domains or [],
        "answer": answer,
        "sources": discovered_sources,
        "discovered": True,
    }
