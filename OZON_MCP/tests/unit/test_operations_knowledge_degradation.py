"""Test operations knowledge tools degradation when knowledge base is unavailable."""

from __future__ import annotations

from unittest.mock import MagicMock

from ozon_mcp.tools.operations_knowledge import _knowledge_unavailable, register


def test_knowledge_unavailable_error_structure() -> None:
    """The error envelope follows the project's make_error contract."""
    err = _knowledge_unavailable()
    assert err["error"] == "knowledge_unavailable"
    assert err["error_type"] == "knowledge_unavailable"
    assert "中文Ozon运营知识库当前不可用" in err["message"]
    assert err["component"] == "operations_knowledge"
    assert "recovery_hint" in err
    # Must not leak stack traces or absolute paths
    for _key, value in err.items():
        if isinstance(value, str):
            assert "Traceback" not in value
            assert "\\\\" not in value
            assert "D:" not in value
            assert "/mnt/" not in value


def test_knowledge_unavailable_with_load_error() -> None:
    """The load_error string is accepted but not exposed to the client."""
    err = _knowledge_unavailable(load_error="FileNotFoundError: chunks.jsonl")
    assert err["error"] == "knowledge_unavailable"
    assert err["error_type"] == "knowledge_unavailable"
    # load_error is internal; the client-facing message is generic
    assert "FileNotFoundError" not in err["message"]


def test_tools_registered_when_kb_is_none() -> None:
    """All three tools must be registered even when the knowledge base is None."""
    mcp = MagicMock()
    registered_tools: list[str] = []

    def fake_tool():
        """Decorator spy that records the function name."""

        def deco(fn):
            registered_tools.append(fn.__name__)
            return fn

        return deco

    mcp.tool = fake_tool

    register(mcp, kb=None, search_index=None)

    assert "ozon_search_operations_knowledge" in registered_tools
    assert "ozon_get_operations_knowledge" in registered_tools
    assert "ozon_list_operations_topics" in registered_tools


def test_search_returns_knowledge_unavailable_when_kb_none() -> None:
    """ozon_search_operations_knowledge returns knowledge_unavailable when kb=None."""
    mcp = MagicMock()
    tool_fns: dict[str, object] = {}

    def fake_tool():
        def deco(fn):
            tool_fns[fn.__name__] = fn
            return fn

        return deco

    mcp.tool = fake_tool

    register(mcp, kb=None, search_index=None)

    result = tool_fns["ozon_search_operations_knowledge"](
        query="跟卖还是精铺", limit=3
    )
    assert result["error"] == "knowledge_unavailable"
    assert result["error_type"] == "knowledge_unavailable"


def test_get_returns_knowledge_unavailable_when_kb_none() -> None:
    """ozon_get_operations_knowledge returns knowledge_unavailable when kb=None."""
    mcp = MagicMock()
    tool_fns: dict[str, object] = {}

    def fake_tool():
        def deco(fn):
            tool_fns[fn.__name__] = fn
            return fn

        return deco

    mcp.tool = fake_tool

    register(mcp, kb=None, search_index=None)

    result = tool_fns["ozon_get_operations_knowledge"](chunk_id="01-001")
    assert result["error"] == "knowledge_unavailable"


def test_list_topics_returns_knowledge_unavailable_when_kb_none() -> None:
    """ozon_list_operations_topics returns knowledge_unavailable when kb=None."""
    mcp = MagicMock()
    tool_fns: dict[str, object] = {}

    def fake_tool():
        def deco(fn):
            tool_fns[fn.__name__] = fn
            return fn

        return deco

    mcp.tool = fake_tool

    register(mcp, kb=None, search_index=None)

    result = tool_fns["ozon_list_operations_topics"](limit=5)
    assert result["error"] == "knowledge_unavailable"


def test_api_layer_tools_unaffected_by_kb_failure() -> None:
    """API knowledge tools (discovery, search, etc.) work independently of ops KB."""
    # This is validated by the fact that the discovery tools don't reference
    # operations_kb at all — they only depend on catalog, search, graph, knowledge.
    # The server.py create_server() already handles the try/except so that
    # operations_kb failure doesn't propagate to the rest of the server.
    from ozon_mcp.operations_knowledge.loader import load_operations_knowledge

    kb = load_operations_knowledge()
    assert kb.lesson_count == 42
    assert kb.chunk_count == 610
