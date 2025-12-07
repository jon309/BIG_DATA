#!/usr/bin/env bash
set -e

echo "[*] Serving analysis results on port 8000..."
cd /app
python3 -m http.server 8000
