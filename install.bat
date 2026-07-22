@echo off
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion

echo ==========================================
echo   TRIZ Innovation Toolkit 安装程序 v2.0
echo ==========================================
echo.

:: 检测 Hermes home
if not defined HERMES_HOME set HERMES_HOME=%USERPROFILE%\.hermes
set SKILLS_DIR=%HERMES_HOME%\skills
set TRIZ_DIR=%SKILLS_DIR%\triz-innovation-toolkit

echo [1/5] Skills 目录: %SKILLS_DIR%

:: 检测 Python 3.12+
set PYTHON=
set PYTHON_VERSION=

:: 检查常见 Python 安装路径
for %%P in (
    "%LOCALAPPDATA%\Programs\Python\Python314\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    "python3.exe"
    "python.exe"
) do (
    if exist %%~P (
        for /f "tokens=*" %%V in ('%%~P -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2^>nul') do (
            set PYTHON_VERSION=%%V
            set PYTHON=%%~P
            goto :found_python
        )
    )
)

:found_python
if not defined PYTHON (
    echo [错误] 需要 Python ^>= 3.12，当前未找到。
    echo   请安装 Python 3.12+: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [2/5] Python: %PYTHON% (%PYTHON_VERSION%)

:: 克隆或更新 Skill
echo [3/5] 安装 Skill 文件...
if exist "%TRIZ_DIR%\.git" (
    echo   目录已存在，更新中...
    cd /d "%TRIZ_DIR%"
    git pull origin main --quiet 2>nul || (
        echo [警告] git pull 失败，跳过更新
    )
) else (
    if not exist "%SKILLS_DIR%" mkdir "%SKILLS_DIR%"
    cd /d "%SKILLS_DIR%"
    git clone https://github.com/fanfanbox/triz-innovation-toolkit.git --quiet
)

:: 安装 triz-ai
echo [4/5] 安装 triz-ai Python 包...
"%PYTHON%" -m pip install triz-ai --quiet 2>nul || (
    echo [警告] triz-ai 安装失败，Skill 知识层仍可使用
)

:: 创建 triz-ai 配置目录
echo [5/5] 初始化配置...
if not exist "%USERPROFILE%\.triz-ai" mkdir "%USERPROFILE%\.triz-ai"

echo.
echo ==========================================
echo   安装完成！
echo ==========================================
echo.
echo Skill 目录: %TRIZ_DIR%
echo.
echo 使用方法:
echo   1. 在 Hermes 中加载: /skill triz-innovation-toolkit
echo   2. 描述你的工程问题
echo   3. AI 自动选择 TRIZ 工具并分析
echo.
echo Triz-AI CLI (可选):
echo   triz-ai analyze "你的问题"
echo   triz-ai discover --domain "你的领域"
echo.
echo 配置 LLM 后端: %%USERPROFILE%%\.triz-ai\config.yaml
echo 详见: https://github.com/fanfanbox/triz-innovation-toolkit
echo.
pause
