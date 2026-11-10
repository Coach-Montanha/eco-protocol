#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
conferir_video.py: O jeito do agente (Claude Code / Antigravity) ver e ouvir o vídeo que ele mesmo editou.
Baseado no guia de Loop de Verificação de Fabiano & Boris Cherny.

Uso:
  python conferir_video.py final.mp4 [--roteiro roteiro.txt] [--ouvido transcricao.txt]
                                     [--formato 1080x1920] [--pausa 0.6] [--saida conferencia] [--sonda]

Grava conferencia/RELATORIO.md, as folhas de quadros (12 quadros/folha) e 1 imagem por corte (antes/depois).
Sai com 0 quando está tudo certo e com 1 quando tem o que consertar.
Requisitos: Python 3 e ffmpeg/ffprobe no PATH.
"""

import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

NUM = {
    "zero": "0", "um": "1", "uma": "1", "dois": "2", "duas": "2", "três": "3", "tres": "3", "quatro": "4",
    "cinco": "5", "seis": "6", "sete": "7", "oito": "8", "nove": "9", "dez": "10", "onze": "11", "doze": "12",
    "treze": "13", "catorze": "14", "quatorze": "14", "quinze": "15", "dezesseis": "16", "dezessete": "17",
    "dezoito": "18", "dezenove": "19", "vinte": "20", "trinta": "30", "quarenta": "40", "cinquenta": "50",
    "sessenta": "60", "setenta": "70", "oitenta": "80", "noventa": "90", "cem": "100", "mil": "1000"
}

def rodar(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")

def ff(video, *filtro):
    cmd = ["ffmpeg", "-nostdin", "-hide_banner", "-i", str(video)] + list(filtro) + ["-f", "null", "-"]
    return rodar(cmd).stderr

def info(video):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration:stream=codec_type,width,height,r_frame_rate",
        "-of", "json", str(video)
    ]
    res = rodar(cmd)
    try:
        d = json.loads(res.stdout)
    except Exception as e:
        sys.stderr.write(f"Erro ao ler informações do vídeo com ffprobe: {e}\nSaída: {res.stderr}\n")
        sys.exit(1)

    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    n, _, m = v.get("r_frame_rate", "0/1").partition("/")
    try:
        fps = float(n) / float(m or 1)
    except Exception:
        fps = 0.0

    duration = float(d.get("format", {}).get("duration", 0.0))
    width = v.get("width")
    height = v.get("height")
    tem_audio = any(s.get("codec_type") == "audio" for s in d.get("streams", []))

    return duration, width, height, fps, tem_audio

def silencios(video, dur):
    err = ff(video, "-vn", "-af", "silencedetect=noise=-35dB:d=0.05")
    ini = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", err)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    return [(max(a, 0.0), fim[i] if i < len(fim) else dur) for i, a in enumerate(ini)]

def pretos(video):
    err = ff(video, "-an", "-vf", "blackdetect=d=0.1:pix_th=0.10")
    return [(float(a), float(b)) for a, b in re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", err)]

def congelados(video):
    err = ff(video, "-an", "-vf", "freezedetect=n=0.003:d=2")
    return [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", err)]

def volume(video):
    err = ff(video, "-vn", "-af", "ebur128=peak=true")
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", err)
    p = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", err)
    return (float(i[-1]) if i else None), (float(p[-1]) if p else None)

def cortes(video):
    err = ff(video, "-an", "-vf", "select='gt(scene,0.35)',showinfo")
    return [float(x) for x in re.findall(r"pts_time:([\d.]+)", err)]

def palavras(texto):
    return [NUM.get(w, w) for w in re.findall(r"[\w']+", texto.lower())]

def plantar_erro(video, dur, pasta):
    # sonda: copia 10 s do meio do vídeo com 1,5 s de tela preta e silêncio plantados em 5 s
    sonda = pasta / "sonda.mp4"
    ini = max(dur / 2.0 - 5.0, 0.0)
    cmd = [
        "ffmpeg", "-nostdin", "-loglevel", "error", "-y",
        "-ss", f"{ini:.2f}", "-t", "10", "-i", str(video),
        "-vf", "drawbox=enable='between(t,5,6.5)':color=black:t=fill",
        "-af", "volume=enable='between(t,5,6.5)':volume=0",
        "-c:v", "libx264", "-preset", "ultrafast", "-c:a", "aac", str(sonda)
    ]
    rodar(cmd)
    return sonda

def main():
    ap = argparse.ArgumentParser(description="Conferidor autônomo de vídeo para agentes de IA")
    ap.add_argument("video", help="Caminho do arquivo MP4 a ser conferido")
    ap.add_argument("--roteiro", help="Caminho do arquivo de roteiro esperado (ex.: roteiro.txt)")
    ap.add_argument("--ouvido", help="Caminho da transcrição ouvida do render (ex.: ouvido.txt)")
    ap.add_argument("--formato", help="Formato esperado, ex.: 1080x1920")
    ap.add_argument("--pausa", type=float, default=0.6, help="Tolerância máxima de silêncio interno em segundos (padrão: 0.6)")
    ap.add_argument("--saida", default="conferencia", help="Pasta de saída dos relatórios e prints (padrão: conferencia)")
    ap.add_argument("--sonda", action="store_true", help="Planta erro artificial para testar se o conferidor não está cego")
    a = ap.parse_args()

    video = Path(a.video)
    if not video.exists():
        sys.stderr.write(f"Erro: Arquivo de vídeo '{video}' não encontrado.\n")
        sys.exit(1)

    out = Path(a.saida)
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True, exist_ok=True)

    falhas, avisos = [], []
    rel = [f"# Conferência de {video.name}", ""]

    dur, w, h, fps, tem_audio = info(video)
    imagem = f"{w}x{h}, {fps:.2f} quadros por segundo" if w else "sem imagem"
    rel += ["## Arquivo", f"{dur:.2f} s, {imagem}, áudio: {'sim' if tem_audio else 'NÃO'}", ""]

    if a.formato and f"{w}x{h}" != a.formato:
        falhas.append(f"formato {w}x{h}, o pedido era {a.formato}")
    if w and h and abs(w / h - 9.0 / 16.0) > 0.01:
        avisos.append(f"proporção {w}x{h} não é 9:16")
    if not tem_audio:
        falhas.append("o vídeo não tem áudio")

    if tem_audio:
        sil = silencios(video, dur)
        comeco = next((b for x, b in sil if x <= 0.01), 0.0)
        final = next((dur - x for x, b in sil if b >= dur - 0.01), 0.0)
        internas = [(x, b) for x, b in sil if x > 0.01 and b < dur - 0.01 and b - x > a.pausa]
        rel += [
            "## Fala, começo e fim",
            f"Primeira fala em {comeco:.2f} s. Depois da última fala sobram {final:.2f} s.",
            f"Pausas acima de {a.pausa} s no meio: {len(internas)}"
        ]
        rel += [f"- {x:.2f} s a {b:.2f} s ({b - x:.2f} s de silêncio)" for x, b in internas] + [""]

        if comeco > 0.5:
            falhas.append(f"a fala só começa em {comeco:.2f} s (tolerância máxima: 0.5 s)")
        if final > 1.2:
            falhas.append(f"sobram {final:.2f} s de silêncio no fim (máximo permitido: 1.2 s)")
        if final < 0.08:
            avisos.append("o áudio termina colado na última fala: confira se a última palavra saiu inteira")
        falhas += [f"espaço demais: {b - x:.2f} s de silêncio em {x:.2f} s" for x, b in internas]

        lufs, pico = volume(video)
        rel += ["## Volume", f"Integrado: {lufs} LUFS. Pico: {pico} dBFS.", ""]
        if lufs is not None and not (-16 <= lufs <= -12):
            avisos.append(f"volume integrado em {lufs} LUFS, fora da faixa recomendada de -16 a -12")
        if pico is not None and pico > -1:
            avisos.append(f"pico em {pico} dBFS, acima do limite seguro de -1 dBFS")

    # Detecção de telas pretas
    pr = [(x, b) for x, b in pretos(video) if x > 0.05 and b < dur - 0.05]
    falhas += [f"tela preta de {b - x:.2f} s em {x:.2f} s" for x, b in pr]

    # Detecção de congelamentos
    avisos += [f"imagem parada por 2 s ou mais a partir de {x:.2f} s" for x in congelados(video)]

    # Detecção e extração de cortes
    cs = cortes(video)
    rel += ["## Cortes", f"{len(cs)} cortes de imagem detectados. Cada corte_NN.jpg mostra 0,2 s antes (esquerda) e 0,2 s depois (direita)."]
    for i, t in enumerate(cs, 1):
        rel.append(f"- corte {i:02d}: {t:.2f} s")
        cmd_corte = [
            "ffmpeg", "-nostdin", "-loglevel", "error",
            "-ss", f"{max(t - 0.2, 0):.2f}", "-i", str(video),
            "-ss", f"{t + 0.2:.2f}", "-i", str(video),
            "-filter_complex", "[0:v]scale=360:-2[a];[1:v]scale=360:-2[b];[a][b]hstack",
            "-frames:v", "1", "-q:v", "4", "-y",
            str(out / f"corte_{i:02d}.jpg")
        ]
        rodar(cmd_corte)

    # Extração de folhas de contato (contact sheets)
    cmd_folhas = [
        "ffmpeg", "-nostdin", "-loglevel", "error", "-i", str(video),
        "-vf", "fps=1/2,scale=270:-2,tile=4x3", "-q:v", "4", "-y",
        str(out / "folha_%02d.jpg")
    ]
    rodar(cmd_folhas)
    rel += [
        "", "## Folhas de quadros",
        "1 quadro a cada 2 s, 12 quadros por folha (grid 4x3), da esquerda pra direita e de cima pra baixo: "
        "a folha_01 vai de 0 a 22 s, a folha_02 de 24 a 46 s, e assim por diante.", ""
    ]

    # Comparação de roteiro vs fala ouvida
    if a.roteiro and a.ouvido:
        p_rot, p_ouv = Path(a.roteiro), Path(a.ouvido)
        if p_rot.exists() and p_ouv.exists():
            e = palavras(p_rot.read_text(encoding="utf-8", errors="ignore"))
            o = palavras(p_ouv.read_text(encoding="utf-8", errors="ignore"))
            dif = [
                (op, " ".join(e[i1:i2]), " ".join(o[j1:j2]))
                for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=e, b=o, autojunk=False).get_opcodes()
                if op != "equal"
            ]
            rel += ["## Roteiro contra o que se ouve", f"Esperadas {len(e)} palavras, ouvidas {len(o)}. Diferenças encontradas: {len(dif)}"]
            nome = {"replace": "trocou", "delete": "faltou", "insert": "sobrou"}
            rel += [f"- {nome.get(op, op)}: esperado '{x}', ouvido '{y}'" for op, x, y in dif] + [""]
            falhas += [f"fala diferente do roteiro: esperado '{x}', ouvido '{y}'" for op, x, y in dif]

    # Teste de sonda (erro plantado artificialmente)
    if a.sonda:
        with tempfile.TemporaryDirectory() as tmp:
            s = plantar_erro(video, dur, Path(tmp))
            pegou_preto = any(4.8 <= x <= 5.2 for x, b in pretos(s))
            pegou_som = any(4.8 <= x <= 5.2 and b - x > a.pausa for x, b in silencios(s, 10.0)) if tem_audio else True
        ok = pegou_preto and pegou_som
        rel += ["## Sonda de Validação", f"Erro plantado (1,5 s de tela preta e silêncio): {'PEGO' if ok else 'NÃO FOI PEGO'}", ""]
        if not ok:
            falhas.append("a sonda com erro plantado passou sem ser pega: o conferidor está cego e não pode ser confiado")

    rel += ["## Avisos"] + ([f"- {x}" for x in avisos] if avisos else ["- Nenhum aviso"]) + ["", "## Veredito"]
    if not falhas:
        rel += ["APROVADO"]
    else:
        rel += ["CONSERTAR"] + [f"- {x}" for x in falhas]

    relatorio_txt = "\n".join(rel) + "\n"
    (out / "RELATORIO.md").write_text(relatorio_txt, encoding="utf-8")
    print(relatorio_txt)

    # Código de saída: 0 para aprovado, 1 para consertar
    sys.exit(1 if falhas else 0)

if __name__ == "__main__":
    main()
