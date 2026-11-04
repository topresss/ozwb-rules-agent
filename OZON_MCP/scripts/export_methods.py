"""Export the complete Ozon API method catalog.

Outputs:
- exports/ozon_methods_full.json
- exports/ozon_methods_index.csv
- exports/ozon_methods_catalog.md
- exports/ozon_methods_tree.txt
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from ozon_mcp.schema import load_catalog

OUTPUT_DIR = Path("exports")


def clean_text(value: Any) -> str:
    """Convert text to one line for CSV and Markdown."""
    if value is None:
        return ""
    return " ".join(str(value).replace("|", "\\|").split())


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 从本地 Seller + Performance Swagger 构建完整目录
    catalog = load_catalog()

    methods = sorted(
        catalog.methods,
        key=lambda item: (
            item.api,
            item.section,
            item.path,
            item.method,
            item.operation_id,
        ),
    )

    seller_count = sum(1 for item in methods if item.api == "seller")
    performance_count = sum(1 for item in methods if item.api == "performance")

    # ------------------------------------------------------------
    # 1. 完整 JSON
    # 包含请求 Schema、响应 Schema、参数、安全等级等全部信息
    # ------------------------------------------------------------

    full_json = {
        "total_methods": catalog.total_methods,
        "seller_methods": seller_count,
        "performance_methods": performance_count,
        "methods": [
            method.model_dump(mode="json")
            for method in methods
        ],
    }

    json_path = OUTPUT_DIR / "ozon_methods_full.json"
    json_path.write_text(
        json.dumps(full_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ------------------------------------------------------------
    # 2. CSV 索引
    # 适合使用 Excel 筛选、统计和查找
    # ------------------------------------------------------------

    csv_path = OUTPUT_DIR / "ozon_methods_index.csv"

    csv_fields = [
        "number",
        "api",
        "section",
        "tag",
        "operation_id",
        "http_method",
        "path",
        "summary",
        "description",
        "safety",
        "safety_reason",
        "deprecated",
        "subscription_min_tier",
        "subscription_tiers_mentioned",
        "auth_type",
        "has_request_schema",
        "response_status_codes",
    ]

    # utf-8-sig：让 Windows Excel 正确显示俄语和中文
    with csv_path.open(
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        writer = csv.DictWriter(file, fieldnames=csv_fields)
        writer.writeheader()

        for number, method in enumerate(methods, start=1):
            writer.writerow(
                {
                    "number": number,
                    "api": method.api,
                    "section": method.section,
                    "tag": method.tag,
                    "operation_id": method.operation_id,
                    "http_method": method.method,
                    "path": method.path,
                    "summary": clean_text(method.summary),
                    "description": clean_text(method.description),
                    "safety": method.safety,
                    "safety_reason": clean_text(method.safety_reason),
                    "deprecated": method.deprecated,
                    "subscription_min_tier": (
                        method.subscription_min_tier or ""
                    ),
                    "subscription_tiers_mentioned": ",".join(
                        method.subscription_tiers_mentioned
                    ),
                    "auth_type": method.auth_type,
                    "has_request_schema": bool(method.request_schema),
                    "response_status_codes": ",".join(
                        method.response_schemas.keys()
                    ),
                }
            )

    # ------------------------------------------------------------
    # 3. Markdown 完整目录
    # 按 API 和 section 分组
    # ------------------------------------------------------------

    grouped: dict[str, dict[str, list[Any]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for method in methods:
        grouped[method.api][method.section].append(method)

    markdown_lines: list[str] = [
        "# Ozon API 完整方法目录",
        "",
        f"- 方法总数：**{catalog.total_methods}**",
        f"- Seller API：**{seller_count}**",
        f"- Performance API：**{performance_count}**",
        "",
    ]

    for api_name in ("seller", "performance"):
        api_methods = [
            method for method in methods
            if method.api == api_name
        ]

        markdown_lines.extend(
            [
                f"## {api_name.upper()} API",
                "",
                f"方法数量：**{len(api_methods)}**",
                "",
            ]
        )

        sections = grouped.get(api_name, {})

        for section_name in sorted(sections):
            section_methods = sections[section_name]

            markdown_lines.extend(
                [
                    f"### {clean_text(section_name)}",
                    "",
                    f"方法数量：**{len(section_methods)}**",
                    "",
                    "| # | Operation ID | HTTP | Path | 安全级别 | 订阅提示 | 说明 |",
                    "|---:|---|---|---|---|---|---|",
                ]
            )

            for index, method in enumerate(section_methods, start=1):
                subscription = method.subscription_min_tier or "-"
                summary = clean_text(method.summary) or "-"

                markdown_lines.append(
                    f"| {index} "
                    f"| `{method.operation_id}` "
                    f"| `{method.method}` "
                    f"| `{method.path}` "
                    f"| `{method.safety}` "
                    f"| `{subscription}` "
                    f"| {summary} |"
                )

            markdown_lines.append("")

    markdown_path = OUTPUT_DIR / "ozon_methods_catalog.md"
    markdown_path.write_text(
        "\n".join(markdown_lines),
        encoding="utf-8",
    )

    # ------------------------------------------------------------
    # 4. 纯文本结构树
    # ------------------------------------------------------------

    tree_lines: list[str] = [
        f"ozon-api-methods ({catalog.total_methods})",
    ]

    api_order = ("seller", "performance")

    for api_index, api_name in enumerate(api_order):
        api_is_last = api_index == len(api_order) - 1
        api_branch = "└─" if api_is_last else "├─"

        api_methods = [
            method for method in methods
            if method.api == api_name
        ]

        tree_lines.append(
            f"{api_branch} {api_name.upper()} API ({len(api_methods)})"
        )

        sections = sorted(grouped.get(api_name, {}).items())
        api_indent = "   " if api_is_last else "│  "

        for section_index, (section_name, section_methods) in enumerate(
            sections
        ):
            section_is_last = section_index == len(sections) - 1
            section_branch = "└─" if section_is_last else "├─"

            tree_lines.append(
                f"{api_indent}{section_branch} "
                f"{section_name} ({len(section_methods)})"
            )

            section_indent = (
                api_indent + ("   " if section_is_last else "│  ")
            )

            for method_index, method in enumerate(section_methods):
                method_is_last = method_index == len(section_methods) - 1
                method_branch = "└─" if method_is_last else "├─"

                tree_lines.append(
                    f"{section_indent}{method_branch} "
                    f"{method.operation_id} "
                    f"[{method.method} {method.path}] "
                    f"[{method.safety}]"
                )

    tree_path = OUTPUT_DIR / "ozon_methods_tree.txt"
    tree_path.write_text(
        "\n".join(tree_lines),
        encoding="utf-8",
    )

    print("=" * 60)
    print("Ozon API 方法目录导出成功")
    print("=" * 60)
    print(f"方法总数：{catalog.total_methods}")
    print(f"Seller API：{seller_count}")
    print(f"Performance API：{performance_count}")
    print()
    print(f"完整 JSON：{json_path.resolve()}")
    print(f"Excel CSV：{csv_path.resolve()}")
    print(f"Markdown：{markdown_path.resolve()}")
    print(f"结构树：{tree_path.resolve()}")
    print("=" * 60)


if __name__ == "__main__":
    main()
