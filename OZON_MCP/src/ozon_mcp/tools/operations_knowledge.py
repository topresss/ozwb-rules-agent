"""MCP tools for Chinese Ozon operations knowledge base retrieval."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ozon_mcp.operations_knowledge.models import OperationsKnowledgeBase
from ozon_mcp.operations_knowledge.search import OperationsKnowledgeSearchIndex
from ozon_mcp.schema.errors import make_error


def _knowledge_unavailable(load_error: str | None = None) -> dict[str, Any]:
    return make_error(
        "knowledge_unavailable",
        "中文Ozon运营知识库当前不可用，请检查知识库资源是否完整并重新启动MCP Server。",
        component="operations_knowledge",
        recovery_hint="检查 src/ozon_mcp/operations_knowledge/data/ 下的 manifest.yaml、chunks.jsonl、topics.json 是否完整，然后重启 MCP Server。",
    )


def register(
    mcp: FastMCP,
    kb: OperationsKnowledgeBase | None,
    search_index: OperationsKnowledgeSearchIndex | None,
    load_error: str | None = None,
) -> None:
    _available = kb is not None and search_index is not None

    @mcp.tool()
    def ozon_search_operations_knowledge(
        query: str,
        limit: int = 5,
        module: str | None = None,
        lesson_id: str | None = None,
        verification_required: bool | None = None,
    ) -> dict[str, Any]:
        """搜索中文Ozon运营知识库。

        适用于经营模式、跟卖、精铺、选品、商品卡、定价、仓库、物流、货代、
        促销、广告、履约、售后和风险问题。先搜索获取相关片段ID，再使用
        ozon_get_operations_knowledge 读取完整证据。

        Args:
            query: 搜索关键词（中文），例如"跟卖怎么选品""精铺差异化""货代发货流程"
            limit: 返回结果数量（默认5，最大10）
            module: 可选，按模块筛选
            lesson_id: 可选，按课程ID筛选
            verification_required: 可选，筛选需要时效复核的片段
        """
        if not _available:
            return _knowledge_unavailable(load_error)
        assert search_index is not None, "search_index must be available when _available is True"

        if not query or not query.strip():
            return {
                "query": query,
                "count": 0,
                "error": "query 不能为空",
                "filters": {"limit": limit, "module": module, "lesson_id": lesson_id},
                "results": [],
                "usage_note": "搜索结果属于课程运营经验，不等同于Ozon当前官方规则。涉及佣金、费用、物流时效和政策时，请结合Ozon官方文档复核。",
            }

        results = search_index.search(
            query=query,
            limit=limit,
            module=module,
            lesson_id=lesson_id,
            verification_required=verification_required,
        )

        return {
            "query": query,
            "count": len(results),
            "filters": {
                "limit": limit,
                "module": module,
                "lesson_id": lesson_id,
                "verification_required": verification_required,
            },
            "results": [
                {
                    "chunk_id": r.chunk_id,
                    "lesson_id": r.lesson_id,
                    "lesson_title": r.lesson_title,
                    "module": r.module,
                    "chunk_title": r.chunk_title,
                    "summary": r.summary,
                    "excerpt": r.excerpt,
                    "keywords": r.keywords,
                    "score": r.score,
                    "source_name": r.source_name,
                    "source_type": r.source_type,
                    "source_section": r.source_section,
                    "verification_required": r.verification_required,
                    "verification_reason": r.verification_reason,
                    "time_sensitive_terms": r.time_sensitive_terms,
                }
                for r in results
            ],
            "usage_note": "搜索结果属于课程运营经验，不等同于Ozon当前官方规则。涉及佣金、费用、物流时效和政策时，请结合Ozon官方文档复核。",
        }

    @mcp.tool()
    def ozon_get_operations_knowledge(chunk_id: str) -> dict[str, Any]:
        """根据chunk_id读取一个完整的Ozon运营知识片段。

        应在 ozon_search_operations_knowledge 返回相关chunk_id后调用，
        用于取得完整证据并组织客户答案。

        Args:
            chunk_id: 知识片段ID，来自搜索结果的chunk_id字段
        """
        if not _available:
            return _knowledge_unavailable(load_error)
        assert kb is not None, "kb must be available when _available is True"

        chunk = kb.get_chunk(chunk_id)
        if chunk is None:
            return make_error(
                "not_found",
                f"chunk_id {chunk_id!r} 不存在",
                chunk_id=chunk_id,
                error=f"chunk_id {chunk_id!r} 不存在",
            )

        return {
            "chunk_id": chunk.chunk_id,
            "lesson_id": chunk.lesson_id,
            "lesson_title": chunk.lesson_title,
            "module": chunk.module,
            "chunk_title": chunk.chunk_title,
            "lesson_summary": chunk.lesson_summary,
            "summary": chunk.summary,
            "content": chunk.content,
            "keywords": chunk.keywords,
            "search_aliases": chunk.search_aliases,
            "source_name": chunk.source_name,
            "source_type": chunk.source_type,
            "source_section": chunk.source_section,
            "verification_required": chunk.verification_required,
            "verification_reason": chunk.verification_reason,
            "time_sensitive_terms": chunk.time_sensitive_terms,
        }

    @mcp.tool()
    def ozon_list_operations_topics(
        query: str | None = None,
        module: str | None = None,
        limit: int = 20,
        offset: int = 0,
        include_chunk_ids: bool = False,
    ) -> dict[str, Any]:
        """列出中文Ozon运营知识库的课程目录和主题。

        可按模块、课程标题或关键词筛选，用于了解知识库覆盖范围。

        Args:
            query: 可选，按课程标题或关键词筛选
            module: 可选，按模块筛选
            limit: 返回数量（默认20）
            offset: 分页偏移（默认0）
            include_chunk_ids: 是否返回chunk_id列表（默认false，避免上下文过大）
        """
        if not _available:
            return _knowledge_unavailable(load_error)
        assert kb is not None, "kb must be available when _available is True"

        topics = kb.list_topics()
        filtered = []
        for t in topics:
            if module and t.module != module:
                continue
            if query:
                q = query.lower()
                in_title = q in t.lesson_title.lower()
                in_keywords = any(q in kw.lower() for kw in t.keywords)
                in_summary = q in t.summary.lower()
                in_aliases = any(q in a.lower() for a in t.search_aliases)
                if not (in_title or in_keywords or in_summary or in_aliases):
                    continue
            filtered.append(t)

        total = len(filtered)
        page = filtered[offset : offset + limit]

        return {
            "total_lessons": len(topics),
            "filtered_count": total,
            "offset": offset,
            "limit": limit,
            "modules": sorted({t.module for t in topics if t.module}),
            "topics": [
                {
                    "lesson_id": t.lesson_id,
                    "lesson_title": t.lesson_title,
                    "module": t.module,
                    "summary": t.summary,
                    "keywords": t.keywords,
                    "chunk_count": t.chunk_count,
                    "search_aliases": t.search_aliases,
                    **({"chunk_ids": t.chunk_ids} if include_chunk_ids else {}),
                }
                for t in page
            ],
        }
