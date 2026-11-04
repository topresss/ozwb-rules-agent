# 更新日志

## [0.1.1]

### 修复

- 修复运营知识库加载失败时三个 MCP 工具不注册的问题；新增 `knowledge_unavailable` 可控降级
- 修复中文知识摘要 `_extract_excerpt` 异常扩张问题，增加长度安全帽
- 强化 8 个黄金检索测试，移除弱断言 `or len(results) > 0`
- 补齐搜索结果中的 `source_name`、`source_type`、`source_section` 来源字段
- 修正 `pyproject.toml` 项目链接指向当前仓库

### 文档

- 优化 README 顶部项目图片为全宽显示
- 调整联系方式为克制样式
- 新增 CI 工作流（知识库校验、Ruff、MyPy、pytest、Wheel 构建验证）
- 补充 `knowledge_unavailable` 错误说明

## [0.1.0]

### 新增

- 内置 42 节中文 Ozon 运营知识库（课程运营经验）
- 新增 610 个稳定知识片段，支持 BM25 中文检索
- 新增 3 个运营知识 MCP 工具：`ozon_search_operations_knowledge`、`ozon_get_operations_knowledge`、`ozon_list_operations_topics`
- 新增中文分词器（二元/三元切词 + 业务术语保护）
- 新增课程来源与时效性标记（verification_required + time_sensitive_terms）
- 新增客户问答 Agent 规则（FastMCP instructions）
- 新增知识库校验脚本 `scripts/validate_operations_knowledge.py`
- Wheel 和 Docker 镜像内置知识库资源

### 文档

- README 新增「中文 Ozon 运营知识库」章节
- 更新架构图、项目结构、工具表和调用示例
- 增加课程经验与官方规则边界说明
- 新增 `docs/Ozon客户问答Agent系统提示词.md`

## [0.0.2]

### 变更

- 项目版本从 v0.6.0 调整为 v0.0.2，作为独立开源版本重新发布
- 完整重写中文 README，补充安装、配置、使用场景和常见问题章节
- 新增 `.env.example` 环境变量配置示例
- 新增 `SECURITY.md` 安全策略文档
- 新增 `.gitignore`，排除 `.venv`、`__pycache__`、`exports/` 等本地文件
- 清理 `src/` 下的 `__pycache__` 目录
