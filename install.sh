#!/bin/bash
# TRIZ Innovation Toolkit — 一键安装脚本
# 用法: curl -fsSL https://raw.githubusercontent.com/fanfanbox/triz-innovation-toolkit/main/install.sh | bash
# 或:   bash install.sh

set -e

echo "=========================================="
echo "  TRIZ Innovation Toolkit 安装程序 v2.0"
echo "=========================================="
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检测操作系统
OS="$(uname -s)"
case "$OS" in
    Linux*)     PLATFORM="linux";;
    Darwin*)    PLATFORM="macos";;
    MINGW*|MSYS*|CYGWIN*) PLATFORM="windows";;
    *)          PLATFORM="unknown";;
esac
echo -e "${GREEN}[1/5]${NC} 检测平台: $PLATFORM"

# 检测 Hermes home
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
SKILLS_DIR="$HERMES_HOME/skills"
TRIZ_DIR="$SKILLS_DIR/triz-innovation-toolkit"

echo -e "${GREEN}[2/5]${NC} Skills 目录: $SKILLS_DIR"

# 检测 Python
PYTHON=""
PYTHON_VERSION=""

# 优先查找 Python 3.12+
for py in python3.14 python3.13 python3.12 python3 python; do
    if command -v "$py" &> /dev/null; then
        ver=$("$py" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        major=$(echo "$ver" | cut -d. -f1)
        minor=$(echo "$ver" | cut -d. -f2)
        if [ "$major" -ge 3 ] && [ "$minor" -ge 12 ]; then
            PYTHON="$py"
            PYTHON_VERSION="$ver"
            break
        fi
    fi
done

# Windows 特殊路径
if [ -z "$PYTHON" ] && [ "$PLATFORM" = "windows" ]; then
    for py in "/c/Users/$USERNAME/AppData/Local/Programs/Python/Python314/python.exe" \
              "/c/Users/$USERNAME/AppData/Local/Programs/Python/Python313/python.exe" \
              "/c/Users/$USERNAME/AppData/Local/Programs/Python/Python312/python.exe"; do
        if [ -f "$py" ]; then
            ver=$("$py" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
            PYTHON="$py"
            PYTHON_VERSION="$ver"
            break
        fi
    done
fi

if [ -z "$PYTHON" ]; then
    echo -e "${RED}[错误]${NC} 需要 Python >= 3.12，当前未找到。"
    echo "  请安装 Python 3.12+: https://www.python.org/downloads/"
    exit 1
fi
echo -e "${GREEN}[3/5]${NC} Python: $PYTHON ($PYTHON_VERSION)"

# 克隆 Skill 文件
echo -e "${GREEN}[4/5]${NC} 安装 Skill 文件..."
if [ -d "$TRIZ_DIR" ]; then
    echo "  目录已存在，更新中..."
    cd "$TRIZ_DIR"
    git pull origin main --quiet 2>/dev/null || {
        echo -e "${YELLOW}[警告]${NC} git pull 失败，尝试重新克隆..."
        cd "$SKILLS_DIR"
        rm -rf "$TRIZ_DIR"
        git clone https://github.com/fanfanbox/triz-innovation-toolkit.git --quiet
    }
else
    mkdir -p "$SKILLS_DIR"
    cd "$SKILLS_DIR"
    git clone https://github.com/fanfanbox/triz-innovation-toolkit.git --quiet
fi

# 安装 triz-ai Python 包
echo -e "${GREEN}[5/5]${NC} 安装 triz-ai Python 包..."
if command -v uv &> /dev/null; then
    uv pip install triz-ai --python "$PYTHON" --quiet 2>/dev/null || \
    "$PYTHON" -m pip install triz-ai --quiet 2>/dev/null || {
        echo -e "${YELLOW}[警告]${NC} triz-ai 安装失败（需要 Python >= 3.12）"
        echo "  Skill 知识层仍可使用，Triz-AI CLI 功能将降级"
    }
else
    "$PYTHON" -m pip install triz-ai --quiet 2>/dev/null || {
        echo -e "${YELLOW}[警告]${NC} triz-ai 安装失败（需要 Python >= 3.12）"
        echo "  Skill 知识层仍可使用，Triz-AI CLI 功能将降级"
    }
fi

echo ""
echo "=========================================="
echo -e "  ${GREEN}安装完成！${NC}"
echo "=========================================="
echo ""
echo "Skill 目录: $TRIZ_DIR"
echo ""
echo "使用方法:"
echo "  1. 在 Hermes 中加载: /skill triz-innovation-toolkit"
echo "  2. 描述你的工程问题"
echo "  3. AI 自动选择 TRIZ 工具并分析"
echo ""
echo "Triz-AI CLI (可选):"
echo "  triz-ai analyze \"你的问题\""
echo "  triz-ai discover --domain \"你的领域\""
echo ""
echo "配置 LLM 后端: ~/.triz-ai/config.yaml"
echo "详见: https://github.com/fanfanbox/triz-innovation-toolkit#triz-ai-cli-配置"
