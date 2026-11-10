#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testar_sonda.py: Cria uma cópia com erros deliberados para testar se a conferência realmente reprova.
"Conferência que nunca reprova não está conferindo nada".

Gera 'teste-com-erro.mp4' com 12 segundos e 3 erros intencionais:
1. 0,8 s mudo no começo (limite tolerado é 0,5 s)
2. 1,3 s de silêncio no meio (entre 4 s e 5,3 s)
3. 0,4 s de tela preta entre 8 s e 8,4 s
"""

import subprocess
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Uso: python testar_sonda.py render/final.mp4 [saida-com-erro.mp4]")
        sys.exit(1)

    video_origem = sys.argv[1]
    video_saida = sys.argv[2] if len(sys.argv) > 2 else "teste-com-erro.mp4"

    cmd = [
        "ffmpeg", "-y", "-t", "12", "-i", video_origem,
        "-vf", "drawbox=enable='between(t,8,8.4)':color=black:t=fill",
        "-af", "volume=enable='between(t,0,0.8)+between(t,4,5.3)':volume=0",
        "-c:v", "libx264", "-c:a", "aac", video_saida
    ]

    print(f"Gerando vídeo com erro plantado a partir de {video_origem} -> {video_saida}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("Vídeo com erro gerado com sucesso!")
        print(f"Agora teste: python conferir_video.py {video_saida} --saida conferencia-teste --sonda")
        print("Esperado: status CONSERTAR com 3 erros listados e sonda APROVADA.")
    else:
        print("Erro ao gerar vídeo com erro plantado:", res.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
