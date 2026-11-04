"""Test Chinese tokenizer for operations knowledge."""

from __future__ import annotations

from ozon_mcp.operations_knowledge.tokenizer import tokenize


def test_business_terms_preserved() -> None:
    tokens = tokenize("跟卖怎么做")
    assert "跟卖" in tokens, f"tokens: {tokens}"

    tokens2 = tokenize("精铺和铺货的区别")
    assert "精铺" in tokens2, f"tokens: {tokens2}"
    assert "铺货" in tokens2, f"tokens: {tokens2}"


def test_rfbs_case_insensitive() -> None:
    tokens = tokenize("rFBS发货流程")
    assert any("rFBS" in t or "rfbs" in t.lower() for t in tokens), f"tokens: {tokens}"


def test_product_card_term() -> None:
    tokens = tokenize("商品卡优化技巧")
    assert "商品卡" in tokens, f"tokens: {tokens}"


def test_bigrams_produced() -> None:
    tokens = tokenize("精铺差异化")
    has_bigram = any(len(t) >= 2 for t in tokens if "一" <= t[0] <= "鿿")
    assert has_bigram, f"tokens: {tokens}"


def test_mixed_cn_en() -> None:
    tokens = tokenize("Ozon FBS仓库怎么设置")
    assert len(tokens) > 0
    assert any("ozon" in t.lower() for t in tokens), f"tokens: {tokens}"
    assert "FBS" in tokens or "fbs" in [t.lower() for t in tokens], f"tokens: {tokens}"


def test_empty_string_no_tokens() -> None:
    assert tokenize("") == []
    assert tokenize("   ") == []
