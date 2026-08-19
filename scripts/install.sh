#!/bin/bash
# Patent Search Engine - 安装脚本
# ================================
# 用法: bash install.sh [--full]

set -e

echo "========================================"
echo "Patent Search Engine 安装"
echo "========================================"

# 检查 Python 版本
echo ""
echo "检查 Python 环境..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "Python 版本: $python_version"

# 安装基础依赖
echo ""
echo "安装基础依赖..."
pip install requests --quiet
echo "✅ requests 已安装"

# 检查是否安装完整版
if [ "$1" = "--full" ]; then
    echo ""
    echo "安装完整依赖..."
    
    # 混合检索依赖
    echo "安装 sentence-transformers..."
    pip install sentence-transformers numpy --quiet
    echo "✅ sentence-transformers 已安装"
    
    # BigQuery 依赖
    echo "安装 google-cloud-bigquery..."
    pip install google-cloud-bigquery --quiet
    echo "✅ google-cloud-bigquery 已安装"
fi

echo ""
echo "========================================"
echo "安装完成!"
echo "========================================"
echo ""
echo "使用方法:"
echo "  python patent_search.py 'phase change material thermal management'"
echo "  python patent_search.py --domain 'PCM battery' --max 100"
echo ""
echo "配置 API Key (可选):"
echo "  export LENS_API_KEY=your_key        # Lens.org"
echo "  export GOOGLE_API_KEY=your_key      # Google Custom Search"
echo "  export GOOGLE_CLOUD_PROJECT=your_id # BigQuery"
echo ""
