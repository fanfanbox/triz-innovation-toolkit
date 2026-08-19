#!/bin/bash
# TRIZ Report — Markdown to Word Converter
# Usage: bash convert_to_word.sh <input.md> [output.docx]
# Example: bash convert_to_word.sh TRIZ_报告_课题_完整版.md

set -e

INPUT="${1:?Usage: convert_to_word.sh <input.md> [output.docx]}"
OUTPUT="${2:-${INPUT%.md}.docx}"

if [ ! -f "$INPUT" ]; then
  echo "Error: Input file not found: $INPUT"
  exit 1
fi

if ! command -v pandoc &> /dev/null; then
  echo "Error: pandoc is required. Install from https://pandoc.org/installing.html"
  exit 1
fi

echo "Converting: $INPUT -> $OUTPUT"
pandoc "$INPUT" -o "$OUTPUT" --from markdown --to docx

if [ -f "$OUTPUT" ]; then
  SIZE=$(ls -lh "$OUTPUT" | awk '{print $5}')
  echo "Done: $OUTPUT ($SIZE)"
else
  echo "Error: Conversion failed"
  exit 1
fi
