"""BM25 search index for Chinese operations knowledge retrieval."""

from __future__ import annotations

from typing import ClassVar

from rank_bm25 import BM25Okapi

from ozon_mcp.operations_knowledge.models import (
    OperationsKnowledgeBase,
    OperationsKnowledgeChunk,
    OperationsKnowledgeSearchResult,
)
from ozon_mcp.operations_knowledge.tokenizer import tokenize


class OperationsKnowledgeSearchIndex:
    """BM25 search over operations knowledge chunks with field-weighted token repetition.

    Token repetition strategy for field weighting (no external weighting API needed):
    - chunk_title: 6x
    - lesson_title: 5x
    - search_aliases: 5x
    - keywords: 4x
    - module: 3x
    - lesson_summary: 2x
    - summary: 2x
    - content: 1x
    """

    _FIELD_WEIGHTS: ClassVar[dict[str, int]] = {
        "chunk_title": 6,
        "lesson_title": 5,
        "search_aliases": 5,
        "keywords": 4,
        "module": 3,
        "lesson_summary": 2,
        "summary": 2,
        "content": 1,
    }

    def __init__(self, kb: OperationsKnowledgeBase):
        self._kb = kb
        self._chunks: list[OperationsKnowledgeChunk] = []
        self._corpus: list[list[str]] = []
        self._bm25: BM25Okapi | None = None
        self._chunk_ids: list[str] = []
        self._build_index()

    def _build_index(self) -> None:
        for chunk in self._kb.chunks.values():
            tokens: list[str] = []
            for field, weight in self._FIELD_WEIGHTS.items():
                value = getattr(chunk, field, "")
                if isinstance(value, list):
                    value = " ".join(str(v) for v in value)
                if value:
                    field_tokens = tokenize(str(value))
                    tokens.extend(field_tokens * weight)
            self._corpus.append(tokens)
            self._chunks.append(chunk)
            self._chunk_ids.append(chunk.chunk_id)

        if self._corpus:
            self._bm25 = BM25Okapi(self._corpus)

    def search(
        self,
        query: str,
        limit: int = 5,
        module: str | None = None,
        lesson_id: str | None = None,
        verification_required: bool | None = None,
    ) -> list[OperationsKnowledgeSearchResult]:
        """Search the operations knowledge base.

        Args:
            query: Free-text search query (Chinese or mixed).
            limit: Max results (1-10, default 5).
            module: Optional filter by module name.
            lesson_id: Optional filter by lesson_id.
            verification_required: Optional filter by verification_required flag.

        Returns:
            List of search results with scores, excerpts, and metadata.
        """
        if not query or not query.strip():
            return []

        limit = max(1, min(limit, 10))

        if self._bm25 is None:
            return []

        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        raw_scores = self._bm25.get_scores(query_tokens)

        # Build candidate list with filters
        candidates: list[tuple[int, float]] = []
        for idx, score in enumerate(raw_scores):
            chunk = self._chunks[idx]
            if module and chunk.module != module:
                continue
            if lesson_id and chunk.lesson_id != lesson_id:
                continue
            if verification_required is not None and chunk.verification_required != verification_required:
                continue
            candidates.append((idx, float(score)))

        # Re-rank
        query_lower = query.strip().lower()
        reranked: list[tuple[int, float]] = []
        for idx, score in candidates:
            chunk = self._chunks[idx]
            boost = 0.0

            # Strong boost: exact match in search_aliases
            aliases_lower = " ".join(a.lower() for a in chunk.search_aliases)
            if query_lower in aliases_lower:
                boost += 3.0
            # Strong boost: exact match in chunk_title
            if query_lower in chunk.chunk_title.lower():
                boost += 2.5
            # Boost: exact match in lesson_title
            if query_lower in chunk.lesson_title.lower():
                boost += 1.5
            # Boost: exact match in summary
            if query_lower in chunk.summary.lower():
                boost += 1.0
            # Mild boost: match in content
            if query_lower in chunk.content.lower():
                boost += 0.5
            # Keyword coverage boost
            kw_hits = sum(1 for kw in chunk.keywords if kw.lower() in query_lower)
            boost += kw_hits * 0.3

            reranked.append((idx, score + boost))

        # Sort by boosted score descending
        reranked.sort(key=lambda x: x[1], reverse=True)

        results: list[OperationsKnowledgeSearchResult] = []
        for idx, score in reranked[:limit]:
            if score <= 0:
                continue
            chunk = self._chunks[idx]
            excerpt = _extract_excerpt(chunk.content, query, 400)
            results.append(
                OperationsKnowledgeSearchResult(
                    chunk_id=chunk.chunk_id,
                    lesson_id=chunk.lesson_id,
                    lesson_title=chunk.lesson_title,
                    module=chunk.module,
                    chunk_title=chunk.chunk_title,
                    summary=chunk.summary,
                    excerpt=excerpt,
                    keywords=chunk.keywords,
                    score=round(score, 3),
                    source_name=chunk.source_name,
                    source_type=chunk.source_type,
                    source_section=chunk.source_section,
                    verification_required=chunk.verification_required,
                    verification_reason=chunk.verification_reason,
                    time_sensitive_terms=chunk.time_sensitive_terms,
                )
            )

        return results


def _extract_excerpt(content: str, query: str, target_chars: int = 400) -> str:
    """Extract a relevant excerpt from content, centered on query match if possible."""
    if len(content) <= target_chars:
        return content

    query_lower = query.strip().lower()
    index = content.lower().find(query_lower)

    # Fall back to token-level matching
    if index < 0:
        from ozon_mcp.operations_knowledge.tokenizer import tokenize

        for token in tokenize(query):
            if len(token) < 2:
                continue
            index = content.lower().find(token.lower())
            if index >= 0:
                break

    if index < 0:
        return content[:target_chars].rstrip() + "…"

    half = target_chars // 2
    start = max(0, index - half)
    end = min(len(content), start + target_chars)

    # If we hit the end, pull start back to keep target_chars
    if end == len(content):
        start = max(0, end - target_chars)

    excerpt = content[start:end].strip()

    if start > 0:
        excerpt = "…" + excerpt
    if end < len(content):
        excerpt = excerpt + "…"

    # Safety cap: never exceed target_chars + 2 (for ellipsis)
    if len(excerpt) > target_chars + 10:
        excerpt = excerpt[:target_chars] + "…"

    return excerpt
