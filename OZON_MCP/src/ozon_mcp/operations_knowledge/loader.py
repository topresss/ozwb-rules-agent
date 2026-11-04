"""Load and validate the Chinese Ozon operations knowledge base."""

from __future__ import annotations

import importlib.resources
import json
import time
from typing import Any

import structlog

from ozon_mcp.operations_knowledge.models import (
    OperationsKnowledgeBase,
    OperationsKnowledgeChunk,
    OperationsKnowledgeManifest,
    OperationsKnowledgeTopic,
)

log = structlog.get_logger()


class KnowledgeLoadError(RuntimeError):
    """知识库加载失败。"""


def _read_package_text(name: str) -> str:
    ref = importlib.resources.files("ozon_mcp.operations_knowledge.data").joinpath(name)
    return ref.read_text(encoding="utf-8")


def _read_package_binary(name: str) -> bytes:
    ref = importlib.resources.files("ozon_mcp.operations_knowledge.data").joinpath(name)
    return ref.read_bytes()


def load_operations_knowledge() -> OperationsKnowledgeBase:
    t0 = time.monotonic()

    # 1. Load manifest
    manifest_raw = _read_package_text("manifest.yaml")
    manifest = OperationsKnowledgeManifest.model_validate(
        _parse_yaml_simple(manifest_raw)
    )

    # 2. Validate manifest counts
    if manifest.lesson_count != 42:
        raise KnowledgeLoadError(
            f"manifest.lesson_count={manifest.lesson_count}, expected 42"
        )
    if manifest.chunk_count != 610:
        raise KnowledgeLoadError(
            f"manifest.chunk_count={manifest.chunk_count}, expected 610"
        )

    # 3. Load chunks (JSONL)
    chunks_raw = _read_package_text("chunks.jsonl")
    chunks: dict[str, OperationsKnowledgeChunk] = {}
    chunks_by_lesson: dict[str, list[OperationsKnowledgeChunk]] = {}
    for line_no, line in enumerate(chunks_raw.splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            obj = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise KnowledgeLoadError(
                f"chunks.jsonl 第{line_no}行不是合法JSON: {exc}"
            ) from exc
        chunk = OperationsKnowledgeChunk.model_validate(obj)
        if chunk.chunk_id in chunks:
            raise KnowledgeLoadError(
                f"chunk_id 重复: {chunk.chunk_id} (第{line_no}行)"
            )
        chunks[chunk.chunk_id] = chunk
        chunks_by_lesson.setdefault(chunk.lesson_id, []).append(chunk)

    if len(chunks) != 610:
        raise KnowledgeLoadError(
            f"实际加载 {len(chunks)} 个chunk，manifest声明610个"
        )

    # 4. Load topics
    topics_raw = _read_package_text("topics.json")
    topics_data = json.loads(topics_raw)
    if not isinstance(topics_data, list):
        raise KnowledgeLoadError("topics.json 必须是 JSON 数组")
    if len(topics_data) != 42:
        raise KnowledgeLoadError(
            f"topics.json 包含 {len(topics_data)} 个主题，expected 42"
        )

    topics: dict[str, OperationsKnowledgeTopic] = {}
    topic_list: list[OperationsKnowledgeTopic] = []
    total_chunk_refs = 0
    for topic_data in topics_data:
        topic = OperationsKnowledgeTopic.model_validate(topic_data)
        topics[topic.lesson_id] = topic
        topic_list.append(topic)
        total_chunk_refs += len(topic.chunk_ids)
        # Validate all chunk_ids exist
        for cid in topic.chunk_ids:
            if cid not in chunks:
                raise KnowledgeLoadError(
                    f"topic {topic.lesson_id} 引用了不存在的 chunk_id: {cid}"
                )

    if total_chunk_refs != 610:
        raise KnowledgeLoadError(
            f"所有topic的chunk_count之和为{total_chunk_refs}，expected 610"
        )

    # 5. Verify source MD file exists
    try:
        _read_package_text("ozon_operations_knowledge.md")
    except Exception as exc:
        raise KnowledgeLoadError(
            f"原始知识文档 ozon_operations_knowledge.md 无法读取: {exc}"
        ) from exc

    # 6. Verify every chunk has a valid lesson_id
    for chunk in chunks.values():
        if chunk.lesson_id not in topics:
            raise KnowledgeLoadError(
                f"chunk {chunk.chunk_id} 的 lesson_id={chunk.lesson_id} 在topics中不存在"
            )

    verification_count = sum(1 for c in chunks.values() if c.verification_required)

    elapsed_ms = (time.monotonic() - t0) * 1000
    log.info(
        "operations_knowledge_loaded",
        version=manifest.version,
        lessons=len(topics),
        chunks=len(chunks),
        source_type=manifest.source_type,
        verification_required_chunks=verification_count,
        load_duration_ms=round(elapsed_ms, 1),
    )

    return OperationsKnowledgeBase(
        manifest=manifest,
        chunks=chunks,
        chunks_by_lesson=chunks_by_lesson,
        topics=topics,
        topic_list=topic_list,
    )


def _parse_yaml_simple(raw: str) -> dict[str, Any]:
    """Minimal YAML parser — only handles the flat key: value shape of manifest.yaml."""
    import yaml

    result: dict[str, Any] = yaml.safe_load(raw)
    return result
