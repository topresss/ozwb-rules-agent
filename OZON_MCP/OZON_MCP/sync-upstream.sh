#!/bin/bash
set -e

# 上游仓库地址
UPSTREAM_REPO="https://github.com/wbcyclist/OZON_MCP.git"
# 临时目录
TMP_DIR="./.tmp_ozon_mcp_upstream"
# 当前脚本所在目录（OZON_MCP文件夹）
DEST_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

echo "====================================="
echo "Sync upstream OZON_MCP to local folder"
echo "Upstream: $UPSTREAM_REPO"
echo "Target dir: $DEST_DIR"
echo "====================================="

# 清理旧临时目录
rm -rf "$TMP_DIR"

# 克隆上游最新代码
echo "Cloning upstream repository..."
git clone --depth=1 "$UPSTREAM_REPO" "$TMP_DIR"

# 拷贝文件到当前 OZON_MCP 目录
echo "Copy files to target folder, overwrite same files..."
cp -r "$TMP_DIR"/* "$DEST_DIR"/

# 删除临时目录
rm -rf "$TMP_DIR"

echo ""
echo "✅ Sync finished!"
echo "Please check changes:"
echo "    git status"
echo "    git add OZON_MCP/"
echo "    git commit -m 'sync: update OZON_MCP from upstream'"
echo "    git push"

