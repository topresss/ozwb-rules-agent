"""Chinese text tokenizer for BM25 operations knowledge search.

Produces tokens for rank-bm25 indexing. Strategy:
- Unicode NFKC normalisation
- Lowercase English, preserve Chinese
- Bigram + trigram for consecutive CJK characters
- Preserve known business terms as single tokens
- Strip noise whitespace and duplicates
"""

from __future__ import annotations

import re
import unicodedata

# ── Business terms that must be preserved as whole tokens ──────────────
_BUSINESS_TERMS: list[str] = [
    "Ozon", "FBS", "FBO", "FBP", "rFBS", "API", "ERP",
    "跟卖", "精铺", "铺货", "货代", "物流", "仓库", "选品", "选品池",
    "定价", "利润率", "商品卡", "主图", "详情页", "促销", "广告", "推广",
    "退货", "拒收", "禁售", "佣金", "国际面单", "一件代发", "自有货源",
]

# Compile a set of normalized business terms for quick lookup
_NORM_TERMS: set[str] = {unicodedata.normalize("NFKC", t) for t in _BUSINESS_TERMS}
_NORM_TERMS_LOWER: set[str] = {t.lower() for t in _NORM_TERMS}

# Regex patterns
_CJK_RE = re.compile(r"[一-鿿㐀-䶿]+")
_ALNUM_RE = re.compile(r"[a-zA-Z0-9]+")
_MIXED_RE = re.compile(r"[a-zA-Z0-9一-鿿]+")


def tokenize(text: str) -> list[str]:
    """Tokenize Chinese text for BM25 indexing."""
    if not text or not text.strip():
        return []

    text = unicodedata.normalize("NFKC", text.strip())
    tokens: list[str] = []

    # 1. Extract and protect business terms (longest match first)
    term_spans: list[tuple[int, int, str]] = []
    sorted_terms = sorted(_BUSINESS_TERMS, key=len, reverse=True)
    lower_text = text.lower()
    for term in sorted_terms:
        term_lower = term.lower()
        start = 0
        while True:
            idx = lower_text.find(term_lower, start)
            if idx < 0:
                break
            term_spans.append((idx, idx + len(term), term))
            start = idx + 1

    # Sort and deduplicate overlapping spans (keep longest)
    term_spans.sort(key=lambda x: (x[0], -(len(x[2]))))
    merged: list[tuple[int, int, str]] = []
    for span in term_spans:
        if merged and span[0] < merged[-1][1]:
            continue
        merged.append(span)
        tokens.append(span[2])

    # 2. Process remaining text segments
    covered: set[int] = set()
    for s, e, _ in merged:
        covered.update(range(s, e))

    segments: list[str] = []
    seg_start = 0
    for i in range(len(text) + 1):
        if i in covered and seg_start < i:
            segments.append(text[seg_start:i])
            seg_start = i + 1

    for s, e, _ in merged:
        if seg_start < s:
            segments.append(text[seg_start:s])
        seg_start = e
    if seg_start < len(text):
        segments.append(text[seg_start:])

    # 3. Tokenize each segment
    for seg in segments:
        # English/numbers
        for match in _ALNUM_RE.finditer(seg):
            tokens.append(match.group().lower())

        # CJK bigrams + trigrams
        for match in _CJK_RE.finditer(seg):
            cjk = match.group()
            if len(cjk) >= 2:
                for i in range(len(cjk) - 1):
                    tokens.append(cjk[i : i + 2])
            if len(cjk) >= 3:
                for i in range(len(cjk) - 2):
                    tokens.append(cjk[i : i + 3])

    # 4. Drop single-char and empty tokens, deduplicate
    seen: set[str] = set()
    result: list[str] = []
    for t in tokens:
        t = t.strip()
        if len(t) < 2 and t not in _NORM_TERMS and t.lower() not in _NORM_TERMS_LOWER:
            continue
        if t not in seen:
            seen.add(t)
            result.append(t)

    return result
