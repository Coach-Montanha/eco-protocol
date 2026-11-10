#!/bin/bash
# Stop hook: o agente só termina quando o render mais recente passa na conferência.
# Código de saída 2: bloqueia a parada e força o agente a ler os erros e consertar.
# Código de saída 0: permite a finalização da tarefa.

cd "$CLAUDE_PROJECT_DIR" || exit 0

VIDEO=$(ls -t render/*.mp4 2>/dev/null | head -1)
[ -z "$VIDEO" ] && exit 0

# Se o render atual já foi aprovado e não há novo vídeo, libera
[ -f conferencia/APROVADO ] && [ conferencia/APROVADO -nt "$VIDEO" ] && exit 0

EXTRA=""
if [ -f roteiro.txt ]; then
  if [ ! -f ouvido.txt ] || [ ouvido.txt -ot "$VIDEO" ]; then
    echo "Transcreva o render $VIDEO em ouvido.txt antes de terminar, pra conferência comparar com o roteiro.txt." >&2
    exit 2
  fi
  EXTRA="--roteiro roteiro.txt --ouvido ouvido.txt"
fi

mkdir -p .claude

if python3 conferir_video.py "$VIDEO" --formato 1080x1920 $EXTRA > .claude/ultima-conferencia.txt 2>&1; then
  touch conferencia/APROVADO
  exit 0
fi

tail -25 .claude/ultima-conferencia.txt >&2
echo "" >&2
echo "O render $VIDEO NÃO passou na conferência. Leia conferencia/RELATORIO.md, abra as folhas de quadros e cortes, conserte e renderize de novo." >&2
exit 2
