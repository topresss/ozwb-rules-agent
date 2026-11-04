#!/usr/bin/env python3
"""Validate the Chinese Ozon operations knowledge base integrity.

Usage:
    uv run python scripts/validate_operations_knowledge.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "src" / "ozon_mcp" / "operations_knowledge" / "data"


def validate() -> int:
    errors: list[str] = []
    manifest_path = DATA_DIR / "manifest.yaml"
    chunks_path = DATA_DIR / "chunks.jsonl"
    topics_path = DATA_DIR / "topics.json"
    md_path = DATA_DIR / "ozon_operations_knowledge.md"

    # Check files exist
    for name, path in [
        ("manifest.yaml", manifest_path),
        ("chunks.jsonl", chunks_path),
        ("topics.json", topics_path),
        ("ozon_operations_knowledge.md", md_path),
    ]:
        if not path.exists():
            errors.append(f"缺失文件: {name}")

    if errors:
        print("[FAIL] 文件缺失:")
        for e in errors:
            print(f"  {e}")
        return 1

    # Load manifest
    import yaml

    with open(manifest_path, encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    name = manifest.get("name", "未知")
    version = manifest.get("version", "未知")
    expected_lessons = manifest.get("lesson_count", 42)
    expected_chunks = manifest.get("chunk_count", 610)
    source_type = manifest.get("source_type", "未知")

    # Load chunks
    chunks: dict[str, dict] = {}
    missing_fields: set[str] = set()
    chunk_lens: list[int] = []
    verification_count = 0

    with open(chunks_path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                chunk = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"chunks.jsonl 第{line_no}行不是合法JSON: {exc}")
                continue
            cid = chunk.get("chunk_id", "")
            if not cid:
                errors.append(f"chunks.jsonl 第{line_no}行缺少chunk_id")
                continue
            if cid in chunks:
                errors.append(f"chunk_id重复: {cid}")
                continue
            chunks[cid] = chunk
            content = chunk.get("content", "")
            chunk_lens.append(len(content))
            if chunk.get("verification_required"):
                verification_count += 1

    # Load topics
    with open(topics_path, encoding="utf-8") as f:
        topics = json.load(f)

    # Validate
    topic_chunk_refs = 0
    invalid_refs = 0
    for topic in topics:
        topic_chunk_refs += len(topic.get("chunk_ids", []))
        for cid in topic.get("chunk_ids", []):
            if cid not in chunks:
                invalid_refs += 1
                errors.append(f"topic {topic.get('lesson_id','?')} 引用了不存在的chunk_id: {cid}")

    # Print report
    print("=" * 60)
    print("  中文 Ozon 运营知识库校验报告")
    print("=" * 60)
    print(f"  知识库名称:     {name}")
    print(f"  版本:           {version}")
    print(f"  课程数量:       {len(topics)} (预期 {expected_lessons})")
    print(f"  片段数量:       {len(chunks)} (预期 {expected_chunks})")
    print(f"  唯一chunk_id:   {len(chunks)}")
    print(f"  主题数量:       {len(topics)}")
    print(f"  需要时效复核:   {verification_count}")
    print(f"  最短片段:       {min(chunk_lens) if chunk_lens else 0} 字符")
    print(f"  最长片段:       {max(chunk_lens) if chunk_lens else 0} 字符")
    print(f"  平均片段:       {sum(chunk_lens)//len(chunk_lens) if chunk_lens else 0} 字符")
    print(f"  缺失字段:       {len(missing_fields)}")
    print(f"  无效topic引用:  {invalid_refs}")
    print(f"  来源类型:       {source_type}")
    print(f"  原始MD存在:     {'是' if md_path.exists() else '否'}")

    # Check counts
    if len(topics) != expected_lessons:
        errors.append(f"主题数量不符: {len(topics)} ≠ {expected_lessons}")
    if len(chunks) != expected_chunks:
        errors.append(f"片段数量不符: {len(chunks)} ≠ {expected_chunks}")
    if topic_chunk_refs != expected_chunks:
        errors.append(f"topic chunk引用总和: {topic_chunk_refs} ≠ {expected_chunks}")

    passed = len(errors) == 0
    print(f"\n  最终验证:       {'[PASS]' if passed else '[FAIL]'}")
    if errors:
        print("\n  错误详情:")
        for e in errors[:20]:
            print(f"  - {e}")
        if len(errors) > 20:
            print(f"  ... 及其他 {len(errors)-20} 个错误")

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(validate())
