"""MCP tool registration."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ozon_mcp.knowledge import KnowledgeBase
from ozon_mcp.operations_knowledge.models import OperationsKnowledgeBase
from ozon_mcp.operations_knowledge.search import OperationsKnowledgeSearchIndex
from ozon_mcp.schema import Catalog, MethodGraph, SearchIndex
from ozon_mcp.tools import (
    discovery,
    execution,
    reference,
    subscription,
    workflow,
)
from ozon_mcp.tools import (
    graph as graph_tool,
)
from ozon_mcp.tools import (
    operations_knowledge as operations_knowledge_tools,
)
from ozon_mcp.transport.performance import PerformanceClient
from ozon_mcp.transport.seller import SellerClient


def register_all(
    mcp: FastMCP,
    catalog: Catalog,
    search: SearchIndex,
    graph: MethodGraph,
    knowledge: KnowledgeBase,
    *,
    seller_client: SellerClient | None = None,
    performance_client: PerformanceClient | None = None,
    operations_kb: OperationsKnowledgeBase | None = None,
    operations_search: OperationsKnowledgeSearchIndex | None = None,
    operations_load_error: str | None = None,
) -> None:
    discovery.register(mcp, catalog, search, graph=graph, knowledge=knowledge)
    graph_tool.register(mcp, catalog, graph)
    workflow.register(mcp, knowledge)
    reference.register(mcp, catalog, knowledge)
    subscription.register(mcp, catalog, seller_client)
    if seller_client is not None or performance_client is not None:
        execution.register(
            mcp,
            catalog,
            seller_client,
            performance_client,
            knowledge=knowledge,
        )
    # Always register ops knowledge tools — they return knowledge_unavailable
    # when the knowledge base failed to load.
    operations_knowledge_tools.register(
        mcp, operations_kb, operations_search, load_error=operations_load_error,
    )
