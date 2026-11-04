"""Test BM25 operations knowledge search."""

from __future__ import annotations

from ozon_mcp.operations_knowledge.loader import load_operations_knowledge
from ozon_mcp.operations_knowledge.search import OperationsKnowledgeSearchIndex, _extract_excerpt

_kb = load_operations_knowledge()
_search = OperationsKnowledgeSearchIndex(_kb)


# ── Helper ────────────────────────────────────────────────────────────
def assert_lesson_in_top(
    query: str,
    expected_lesson: str,
    top_k: int = 3,
) -> None:
    results = _search.search(query, limit=top_k)
    assert len(results) > 0, f"'{query}' returned no results"
    lesson_ids = [r.lesson_id for r in results]
    assert expected_lesson in lesson_ids, (
        f"'{query}' expected lesson {expected_lesson} in top-{top_k}, "
        f"got {[(r.lesson_id, r.chunk_title, r.score) for r in results]}"
    )
    assert results[0].score > 0
    assert results[0].chunk_id
    assert results[0].source_type == "course_experience"
    assert results[0].excerpt
    # Excerpt should not exceed a reasonable bound
    assert len(results[0].excerpt) < 1000, f"excerpt too long: {len(results[0].excerpt)}"


# ── Basic search ──────────────────────────────────────────────────────
def test_search_returns_results() -> None:
    results = _search.search("跟卖还是精铺", limit=5)
    assert len(results) > 0


def test_limit_respected() -> None:
    results = _search.search("选品", limit=3)
    assert len(results) <= 3


def test_module_filter() -> None:
    results = _search.search("仓库", limit=5)
    assert len(results) > 0


def test_lesson_id_filter() -> None:
    results = _search.search("物流", lesson_id="01", limit=5)
    assert len(results) > 0
    for r in results:
        assert r.lesson_id == "01"


def test_verification_required_filter() -> None:
    results = _search.search("佣金", verification_required=True, limit=3)
    for r in results:
        assert r.verification_required


def test_empty_query_returns_empty() -> None:
    results = _search.search("", limit=5)
    assert len(results) == 0


def test_result_has_required_fields() -> None:
    results = _search.search("精铺怎么选品", limit=1)
    assert len(results) == 1
    r = results[0]
    assert r.chunk_id
    assert r.lesson_id
    assert r.lesson_title
    assert r.score > 0
    assert r.excerpt
    assert r.source_name is not None
    assert r.source_type == "course_experience"
    assert r.source_section is not None


def test_source_fields_present() -> None:
    results = _search.search("定价", limit=3)
    for r in results:
        assert isinstance(r.source_name, str)
        assert r.source_type == "course_experience"
        assert isinstance(r.source_section, str)


# ── Golden queries ────────────────────────────────────────────────────
def test_genmai_vs_jingpu_hits_lesson_03() -> None:
    assert_lesson_in_top("新手先做跟卖还是精铺", "03")


def test_jingpu_diff_hits_lesson_02() -> None:
    assert_lesson_in_top("精铺如何做差异化", "02")


def test_huodai_hits_lesson_01() -> None:
    assert_lesson_in_top("什么是货代", "01")


def test_rfbs_ship_hits_lesson_01() -> None:
    assert_lesson_in_top("rFBS的完整发货流程是什么", "01")


def test_warehouse_hits_lesson_06() -> None:
    assert_lesson_in_top("Ozon仓库怎么设置", "06")


def test_weight_check_hits_lesson_07() -> None:
    assert_lesson_in_top("上架前怎么核实重量", "07")


def test_shangpin_bang_hits_lesson_08() -> None:
    assert_lesson_in_top("上品帮怎么使用", "08")


def test_backend_modules_hits_lesson_09() -> None:
    assert_lesson_in_top("Ozon后台有哪些模块", "09")


# ── Excerpt tests ─────────────────────────────────────────────────────
def test_excerpt_long_chinese_text_not_expanded() -> None:
    content = "测试内容。" * 5000  # ~25k chars
    query = "测试"
    excerpt = _extract_excerpt(content, query, 400)
    assert len(excerpt) < 800, f"excerpt expanded to {len(excerpt)} chars"


def test_excerpt_hit_beginning_only_end_ellipsis() -> None:
    content = "这是开头的内容。" * 100
    query = "这是开头"
    excerpt = _extract_excerpt(content, query, 200)
    assert excerpt.startswith("这是开头")
    assert not excerpt.startswith("…")
    assert excerpt.endswith("…")


def test_excerpt_hit_middle_both_ellipsis() -> None:
    content = "前缀" * 200 + "命中词在这里" + "后缀" * 200
    query = "命中词在这里"
    excerpt = _extract_excerpt(content, query, 200)
    assert excerpt.startswith("…")
    assert excerpt.endswith("…")
    assert "命中词在这里" in excerpt


def test_excerpt_short_content_returned_as_is() -> None:
    content = "短内容"
    excerpt = _extract_excerpt(content, "什么", 400)
    assert excerpt == content


def test_excerpt_no_match_returns_opening() -> None:
    content = "abcdefghij" * 100
    query = "zzzz"
    excerpt = _extract_excerpt(content, query, 100)
    assert excerpt.endswith("…")
    assert len(excerpt) <= 110


def test_excerpt_chinese_keyword_hit() -> None:
    content = "前缀" * 50 + "精铺就是精细化铺货" + "后缀" * 50
    query = "精铺"
    excerpt = _extract_excerpt(content, query, 150)
    assert "精铺" in excerpt
    assert len(excerpt) < 300
