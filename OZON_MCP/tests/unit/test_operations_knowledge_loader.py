"""Test operations knowledge loader and data integrity."""

from __future__ import annotations

from ozon_mcp.operations_knowledge.loader import load_operations_knowledge


def test_loads_42_lessons_610_chunks() -> None:
    kb = load_operations_knowledge()
    assert kb.manifest.lesson_count == 42
    assert kb.manifest.chunk_count == 610
    assert kb.lesson_count == 42
    assert kb.chunk_count == 610


def test_chunk_ids_unique() -> None:
    kb = load_operations_knowledge()
    assert len(kb.chunks) == 610


def test_topics_load_42() -> None:
    kb = load_operations_knowledge()
    assert len(kb.topics) == 42
    assert len(kb.topic_list) == 42


def test_topic_chunk_refs_sum_to_610() -> None:
    kb = load_operations_knowledge()
    total = sum(len(t.chunk_ids) for t in kb.topic_list)
    assert total == 610


def test_all_topic_chunk_ids_exist() -> None:
    kb = load_operations_knowledge()
    for topic in kb.topic_list:
        for cid in topic.chunk_ids:
            assert cid in kb.chunks, f"missing chunk_id: {cid}"


def test_source_type_is_course_experience() -> None:
    kb = load_operations_knowledge()
    for chunk in kb.chunks.values():
        assert chunk.source_type == "course_experience"


def test_chunk_not_empty() -> None:
    kb = load_operations_knowledge()
    for chunk in kb.chunks.values():
        assert chunk.chunk_id
        assert chunk.lesson_id
        assert chunk.content.strip()


def test_get_chunk_returns_chunk() -> None:
    kb = load_operations_knowledge()
    first_id = next(iter(kb.chunks))
    chunk = kb.get_chunk(first_id)
    assert chunk is not None
    assert chunk.chunk_id == first_id


def test_get_chunk_missing_returns_none() -> None:
    kb = load_operations_knowledge()
    assert kb.get_chunk("nonexistent") is None


def test_chunks_for_lesson() -> None:
    kb = load_operations_knowledge()
    first_lesson = kb.topic_list[0]
    chunks = kb.chunks_for_lesson(first_lesson.lesson_id)
    assert len(chunks) > 0
    assert all(c.lesson_id == first_lesson.lesson_id for c in chunks)
