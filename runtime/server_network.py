from __future__ import annotations

import json
import re
from urllib.parse import parse_qs, quote, unquote, urlencode, urlparse


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
    plain = re.sub(r"(?s)<[^>]+>", " ", text)
    plain = re.sub(r"\s+", " ", plain).strip()
    return {"title": title, "excerpt": plain[:limit]}


def fetch_allowed_url(url, allowed_domains, json_get):
    host = normalize_domain(url)
    if not domain_allowed(host, allowed_domains):
        return {"ok": False, "error": f"domain_not_allowed:{host}"}
    try:
        content = json_get(url, headers={"User-Agent": "HomeHub/0.1"})
    except Exception as exc:
        return {"ok": False, "error": f"fetch_failed:{exc}"}
    if isinstance(content, dict):
        return {"ok": True, "url": url, "title": str(content.get("title", "")).strip(), "excerpt": json.dumps(content, ensure_ascii=False)[:420]}
    parsed = strip_html_excerpt(str(content))
    return {"ok": True, "url": url, "title": parsed.get("title", ""), "excerpt": parsed.get("excerpt", "")}


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
    answer = str(result.get("answer", "")).strip()
    sources = result.get("sources", [])
    if locale == "zh-CN":
        if sources:
            return f"{answer}\n来源：{'；'.join(str(item.get('url', '')) for item in sources[:3])}"
        return answer
    if sources:
        return f"{answer}\nSources: {'; '.join(str(item.get('url', '')) for item in sources[:3])}"
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
        return {"ok": True, "url": url, "title": str(content.get("title", "")).strip(), "excerpt": json.dumps(content, ensure_ascii=False)[:420]}
    parsed_content = strip_html_excerpt(str(content))
    return {"ok": True, "url": url, "title": parsed_content.get("title", ""), "excerpt": parsed_content.get("excerpt", "")}


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
