# Triz-AI CLI — Pitfalls & Configuration Guide

## Python Version Conflict (Critical)

triz-ai requires Python >=3.12. Current system has Python 3.11.15 as default.

**Problem**: Running `triz-ai` without path override causes `pydantic_core` import error because Hermes venv (Python 3.11) pollutes `sys.path`.

**Solution**: Always use this prefix before any `triz-ai` command:
```bash
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH"
```

**Install location**: `C:\Users\jianw\AppData\Local\Programs\Python\Python314\Scripts\triz-ai.exe`

---

## Model Name Format (Critical)

triz-ai uses raw OpenAI SDK (not litellm). Model names are sent **as-is** to the API endpoint.

```yaml
# ❌ WRONG — MiMo API returns "Unsupported model openai/mimo-v2.5-pro"
default_model: openai/mimo-v2.5-pro

# ✅ CORRECT — direct model ID
default_model: mimo-v2.5-pro
```

The `provider/model` prefix format only works with `pip install triz-ai[litellm]`.

---

## Embedding API Base (Critical)

If `embeddings.api_base` is not set separately, triz-ai uses `llm.api_base` (MiMo) for embeddings, which fails because MiMo doesn't have embedding models.

```yaml
embeddings:
  model: nomic-embed-text
  dimensions: 768
  api_base: http://localhost:11434/v1  # Ollama endpoint
  api_key: ollama                       # Ollama doesn't validate keys
```

---

## MiMo API Available Models

As of 2026-07-22, MiMo API (`https://api.xiaomimimo.com/v1/models`) supports:
- `mimo-v2.5` — standard model (use for classify_model)
- `mimo-v2.5-pro` — advanced model (use for default_model, deep_model)
- `mimo-v2.5-asr` — speech recognition
- `mimo-v2.5-tts` — text-to-speech

There is NO `mimo-v2-pro` or `mimo-v2-flash` — those names don't exist.

---

## Environment Variable Interpolation

Config supports `${VAR}` and `${VAR:-default}` syntax. If a variable is unset and no default is provided, triz-ai raises `ConfigError`.

**Workaround**: Either:
1. Create `~/.triz-ai/.env` with the variables
2. Hardcode the API key in config.yaml
3. Use `${VAR:-}` for optional fields

---

## Working Config (2026-07-22)

```yaml
# ~/.triz-ai/config.yaml
llm:
  default_model: mimo-v2.5-pro
  classify_model: mimo-v2.5
  deep_model: mimo-v2.5-pro
  reasoning_effort: medium
  api_base: https://api.xiaomimimo.com/v1
  api_key: <from ~/.hermes/.env XIAOMI_API_KEY>

embeddings:
  model: nomic-embed-text
  dimensions: 768
  api_base: http://localhost:11434/v1
  api_key: ollama

database:
  path: ~/.triz-ai/patents.db
```

---

## Ollama Models Installed

- `nomic-embed-text:latest` — 274 MB (embedding, required for triz-ai)
- `qwen2.5vl:3b` — 3.2 GB (vision-language)
- `deepseek-coder:1.3b` — 776 MB (code)

For local LLM analysis, consider installing `ollama pull qwen2.5:7b`.
