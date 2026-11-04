"""Data models for the Chinese Ozon operations knowledge base."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class OperationsKnowledgeManifest(BaseModel):
    name: str
    version: str
    language: str = "zh-CN"
    lesson_count: int
    chunk_count: int
    source_type: str
    source_file: str
    chunks_file: str
    topics_file: str
    generated_at: str = ""
    description: str = ""
    notice: str = ""
    chunking: dict[str, Any] = Field(default_factory=dict)
    retrieval: dict[str, Any] = Field(default_factory=dict)


class OperationsKnowledgeChunk(BaseModel):
    chunk_id: str
    lesson_id: str
    lesson_title: str = ""
    module: str = ""
    chunk_index: int = 0
    chunk_title: str = ""
    lesson_summary: str = ""
    summary: str = ""
    content: str
    keywords: list[str] = Field(default_factory=list)
    source_name: str = ""
    source_type: str = "course_experience"
    source_section: str = ""
    language: str = "zh-CN"
    verification_required: bool = False
    verification_reason: str = ""
    time_sensitive_terms: list[str] = Field(default_factory=list)
    search_aliases: list[str] = Field(default_factory=list)

    @field_validator("verification_reason", mode="before")
    @classmethod
    def coerce_none_to_empty(cls, v: object) -> str:
        if v is None:
            return ""
        return str(v)

    @field_validator("chunk_id", "lesson_id")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError(f"field must not be empty: {v!r}")
        return v

    @field_validator("content")
    @classmethod
    def content_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("content must not be empty")
        return v


class OperationsKnowledgeTopic(BaseModel):
    lesson_id: str
    lesson_title: str = ""
    module: str = ""
    summary: str = ""
    keywords: list[str] = Field(default_factory=list)
    chunk_count: int = 0
    chunk_ids: list[str] = Field(default_factory=list)
    search_aliases: list[str] = Field(default_factory=list)


class OperationsKnowledgeSearchResult(BaseModel):
    chunk_id: str
    lesson_id: str
    lesson_title: str
    module: str
    chunk_title: str
    summary: str
    excerpt: str
    keywords: list[str] = Field(default_factory=list)
    score: float
    source_name: str = ""
    source_type: str = "course_experience"
    source_section: str = ""
    verification_required: bool = False
    verification_reason: str = ""
    time_sensitive_terms: list[str] = Field(default_factory=list)


class OperationsKnowledgeBase(BaseModel):
    manifest: OperationsKnowledgeManifest
    chunks: dict[str, OperationsKnowledgeChunk] = Field(default_factory=dict)
    chunks_by_lesson: dict[str, list[OperationsKnowledgeChunk]] = Field(default_factory=dict)
    topics: dict[str, OperationsKnowledgeTopic] = Field(default_factory=dict)
    topic_list: list[OperationsKnowledgeTopic] = Field(default_factory=list)

    @property
    def lesson_count(self) -> int:
        return len(self.topics)

    @property
    def chunk_count(self) -> int:
        return len(self.chunks)

    def get_chunk(self, chunk_id: str) -> OperationsKnowledgeChunk | None:
        return self.chunks.get(chunk_id)

    def get_topic(self, lesson_id: str) -> OperationsKnowledgeTopic | None:
        return self.topics.get(lesson_id)

    def list_topics(self) -> list[OperationsKnowledgeTopic]:
        return self.topic_list

    def chunks_for_lesson(self, lesson_id: str) -> list[OperationsKnowledgeChunk]:
        return self.chunks_by_lesson.get(lesson_id, [])
