#!/usr/bin/env bash
# Instalador em 1 Linha do Protocolo @eco para Linux / macOS
set -e

TARGET_DIR="$HOME/.gemini/config/plugins/efficiency-toolkit/skills/eco"
RULES_DIR="$HOME/.gemini/config/plugins/efficiency-toolkit/rules"

echo "🌿 Instalando Protocolo @eco..."

mkdir -p "$TARGET_DIR"
mkdir -p "$RULES_DIR"

cp SKILL.md "$TARGET_DIR/SKILL.md"
cp rules/AGENTS.md "$RULES_DIR/AGENTS.md"

echo "✅ Protocolo @eco instalado com sucesso!"
echo "🚀 Agora o seu assistente opera sob ultra-eficiência de tokens (70% a 85% de economia)."
