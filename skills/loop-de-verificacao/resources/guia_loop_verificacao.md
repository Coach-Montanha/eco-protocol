--- PAGE 1 ---
Loop de verificacao no Claude Code: o guia completo pra ele
conferir o proprio trabalho
2 a 3 vezes a qualidade do resultado final: e o que o Boris Cherny, que criou o Claude Code, diz que acontece quando o
Claude tem um jeito de conferir o proprio trabalho, na dica que ele chamou de a mais importante da thread de 2 de
janeiro de 2026. A documentacao oficial explica o porque: o Claude para quando o trabalho parece pronto, e se ele nao
tem nada pra rodar que diga se esta pronto mesmo, quem testa e voce, que vira o gargalo de cada entrega.
O loop de verificacao e dar pro Claude uma checagem que volta passou ou falhou, como um teste, um build, um print do
navegador ou a conferencia de um video renderizado, pra ele fazer, conferir, corrigir e so entao dizer que terminou. O
Claude Code de hoje, na versao 2.1.319, tem 4 jeitos de fechar esse loop, do pedido com prova ao Stop hook que nao
deixa ele parar enquanto a checagem falha, e nenhum deles custa nada alem do plano que voce ja usa.
Nesta pagina esta o guia completo, conferido em 7 de novembro de 2026: 11 passos do CLAUDE.md ao Claude rodando
sozinho com limite, o exemplo da edicao de video montado do zero com o conferidor pronto pra colar, que pegou os 5
erros plantados no teste, o Stop hook que barra render reprovado, a checagem certa pra programacao, trafego pago e
copy, 10 prompts e a conferencia antes de deixar o Claude trabalhar sem voce.
Como montar o loop de verificacao, do pedido com prova ao hook sem
excecao
Do 1 ao 6 e o loop pra qualquer trabalho, do 7 ao 9 e o exemplo da edicao de video montado do zero, e o 10 e o 11
poem um revisor de fora e deixam o Claude rodando sozinho com limite.
1. Atualize o Claude Code e confira o plano
Tudo aqui roda no Claude Code, que vem nos planos pagos a partir do Pro: R$ 110 por mes ou R$ 92 no anual, cobrado em real, e US$
20 por mes na pagina de preco em dolar. A versao de 6 de novembro de 2026 e a 2.1.319, e o /goal, o /verify e os hooks ja vem nela,
sem instalar nada.  1) O /goal e os hooks do projeto so ligam depois que voce confia na pasta, no aviso que aparece na primeira vez
que abre o Claude Code nela  2) O Claude no Chrome pede a extensao Claude in Chrome 1.0.36 ou mais nova e login pelo /login, nao
por chave de API  3) O computer use, que deixa o Claude ver e clicar na tela, e research preview so no macOS e vem no Pro, no Max e
no Ultra  claude update
claude --version  https://code.claude.com/docs/en/setup
2. Escreva no CLAUDE.md como provar que ficou pronto
A documentacao diz que a linha mais util do seu CLAUDE.md e o comando que roda a checagem, porque e com ele que o Claude
confere o proprio trabalho enquanto avanca. Vale pra codigo e vale pra qualquer entrega, seja o comando do teste, o script que confere
o video ou a regua da legenda. Escreva so o que o Claude nao descobre lendo a pasta e mantenha o arquivo abaixo de 200 linhas.  #
acrescenta a secao de conferencia no CLAUDE.md da pasta do projeto
cat >> CLAUDE.md <<'MD'
## Como provar que ficou pronto
- Codigo: npm test e npm run build, os 2 saindo sem erro
- Video: python3 conferir_video.py render/final.mp4 --formato 1080x1920, e o relatorio termina em APROVADO
- Legenda e copy: a regua em regras-copy.md, item por item
- Antes de dizer que terminou, rode a checagem e me mostre o comando e a saida. Se nao deu pra conferir, diga o que faltou.
MD  Atalho: Uma linha como sempre rode o teste antes de terminar funciona quase sempre, mas nao sempre. Quando precisar de
sempre, a resposta e o Stop hook do passo 6.  https://code.claude.com/docs/en/best-practices
3. Peca a prova, nao um terminei
O jeito mais leve de fechar o loop nao pede configuracao: no proprio pedido, diga o que conta como pronto e mande rodar a checagem
ate passar. E peca a prova, o comando que rodou e a saida, ou o print, porque a frase todos os testes passam, sozinha, diz pouco, e ler
a saida e mais rapido que rodar de novo. Pra deixar isso automatico, o Superpowers, de Jesse Vincent, traz a skill
verification-before-completion, cuja regra e nenhuma afirmacao de pronto sem prova nova.  1) No pedido: rode os testes de
autenticacao no fim, continue ate passarem e me mostre a saida  2) O Superpowers tem 15 skills, licenca MIT, 313.953 estrelas e a
versao 7.0.2 de 3 de novembro, conferidos em 7 de novembro de 2026  3) A skill dele lista o que nao vale como prova: a rodada
anterior, o deve passar, o linter passou e o subagente que disse que deu certo  /plugin install superpowers@claude-plugins-official 
https://github.com/obra/superpowers/tree/main/skills/verification-before-completion
4. Mande o Claude abrir e usar o que ele fez
Teste passando nao prova que o app funciona, e por isso o Claude Code traz o /verify, que compila, abre e usa o seu app pra confirmar
que a mudanca faz o que devia. O /run abre o app pra voce ver, e o /run-skill-generator grava a receita de como subir o projeto, pra todo

--- PAGE 2 ---
agente seguir a mesma. E o que o Boris descreve na dica 13 da thread dele: cada mudanca que ele sobe no claude.ai/code e testada
pelo Claude no Chrome, que abre o navegador, testa a interface e repete ate o codigo funcionar.  1) O /verify grava o que funcionou em
.claude/skills/verify/SKILL.md, e desde a versao 2.1.286 uma skill verify na pasta faz o Claude rodar a conferencia antes de cada
commit  2) Site e landing page: o claude --chrome da ao Claude o seu navegador, com print, console e clique  3) App nativo, simulador
do iPhone ou programa sem API: o computer use, que voce liga no /mcp, no servidor computer-use  /run-skill-generator
/verify
# no terminal, pra ele usar o seu navegador
claude --chrome  https://code.claude.com/docs/en/chrome
5. Ponha uma meta com o /goal
O /goal e o loop com um juiz de fora: voce escreve a condicao de pronto e, depois de cada volta, um modelo separado le a conversa e
decide se ela foi cumprida, se ainda falta ou se e impossivel. Enquanto falta, o Claude comeca outra volta sozinho, com o motivo do juiz
como proxima instrucao. Como o juiz nao roda comando nem abre arquivo, escreva a condicao como algo que a saida do proprio
Claude mostra na conversa.  1) Uma meta por sessao, com ate 4.000 caracteres  2) O /goal sozinho mostra a condicao, o tempo, as
voltas, os tokens e o ultimo motivo do juiz  3) Pra rodar sem voce aprovar cada comando, use junto com o auto mode  4) Fora da
conversa, o claude -p com o /goal no pedido roda o loop inteiro numa chamada so  /goal npm test sai com 0, o lint esta limpo e nenhum
outro arquivo de teste mudou, ou pare depois de 20 voltas
# mostra o andamento e tira a meta
/goal
/goal clear  https://code.claude.com/docs/en/goal
6. Trave a saida com um Stop hook
O Stop hook e a versao sem excecao: um comando seu que roda toda vez que o Claude tenta encerrar a vez, e quando ele sai com
codigo 2 o Claude volta ao trabalho com o que o comando escreveu como motivo. Quem garante e o proprio Claude Code, nao o
modelo, entao a vez nao termina enquanto a checagem falha. O exemplo da documentacao trava no typecheck, e voce troca pelo teste
do seu projeto.  1) Depois de 8 continuacoes seguidas sem nenhuma ferramenta usada no meio, o Claude Code libera a parada, e a
variavel CLAUDE_CODE_STOP_HOOK_BLOCK_CAP muda esse teto  2) O /hooks mostra os hooks que carregaram  3) No lugar do
comando da pra usar um hook do tipo prompt, em que outro modelo decide, ou do tipo agent, ainda experimental, que abre um
subagente com ferramentas pra conferir  4) Pra testar, peca uma mudanca que quebra um tipo: em vez de terminar, ele recebe o erro
do compilador e continua  # Stop hook do exemplo oficial: o Claude so termina a vez com o typecheck passando
# (troque pnpm tsc --noEmit pelo teste do seu projeto, como npm test)
mkdir -p .claude
cat > .claude/settings.json <<'JSON'
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "pnpm tsc --noEmit 1>&2 || exit 2" }
        ]
      }
    ]
  }
}
JSON  Atalho: Hook e pra regra sem excecao, e preferencia fica no CLAUDE.md, porque todo hook as vezes dispara quando nao devia
e alguem tem que manter cada um.  https://code.claude.com/docs/en/hooks-guide
7. O exemplo do video: monte o conferidor de video
O Claude nao assiste video: a ferramenta de leitura dele abre imagem, PDF e texto, e e por isso que ele entrega a edicao sem ter visto
1 segundo. O conferidor abaixo da os olhos e os ouvidos que faltam, so com o Python e o ffmpeg: mede o comeco, as pausas, o fim, a
tela preta, a imagem parada, o volume e os cortes, compara o roteiro com o que se ouve e monta as folhas de quadros que o Claude
abre como imagem. Ele grava conferencia/RELATORIO.md e sai com 0 quando aprova e com 1 quando tem conserto.  1) Rodou em 7
de novembro num video de 92 s em 30 s, ja com a sonda, e gerou 4 folhas de quadros e 1 imagem por corte  2) Cada folha_NN.jpg tem
12 quadros, 1 a cada 2 s, e cada corte_NN.jpg mostra 0,2 s antes e 0,2 s depois do corte, lado a lado  3) Com --roteiro e --ouvido ele
compara palavra por palavra, e numero falado por extenso, de zero a mil, bate com o digito, como dez com 10  4) A transcricao do
render vem da ferramenta que voce ja usa, como o ElevenLabs Scribe ou o Whisper, salva em ouvido.txt  5) No Windows, o ffmpeg
entra com winget install Gyan.FFmpeg, e os comandos rodam no Git Bash, o mesmo terminal que os hooks usam la  # Mac: o ffmpeg,
uma vez so
brew install ffmpeg
# cria o conferidor na pasta do projeto de edicao
cat > conferir_video.py <<'PY'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# conferir_video.py: o jeito do Claude ver o video que ele mesmo editou.
# uso: python3 conferir_video.py final.mp4 [--roteiro roteiro.txt] [--ouvido transcricao.txt]
#      [--formato 1080x1920] [--pausa 0.6] [--sonda]
# Grava conferencia/RELATORIO.md, as folhas de quadros e 1 imagem por corte.

--- PAGE 3 ---
# Sai com 0 quando esta tudo certo e com 1 quando tem o que consertar. So precisa do Python 3 e do ffmpeg.
import argparse, difflib, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path
NUM = {"zero": "0", "um": "1", "uma": "1", "dois": "2", "duas": "2", "tres": "3", "tres": "3", "quatro": "4",
       "cinco": "5", "seis": "6", "sete": "7", "oito": "8", "nove": "9", "dez": "10", "onze": "11", "doze": "12",
       "treze": "13", "catorze": "14", "quatorze": "14", "quinze": "15", "dezesseis": "16", "dezessete": "17",
       "dezoito": "18", "dezenove": "19", "vinte": "20", "trinta": "30", "quarenta": "40", "cinquenta": "50",
       "sessenta": "60", "setenta": "70", "oitenta": "80", "noventa": "90", "cem": "100", "mil": "1000"}
def rodar(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)
def ff(video, *filtro):
    return rodar(["ffmpeg", "-nostdin", "-hide_banner", "-i", str(video), *filtro, "-f", "null", "-"]).stderr
def info(video):
    d = json.loads(rodar(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height,r_frame_rate",
                          "-of", "json", str(video)]).stdout)
    v = next((s for s in d["streams"] if s["codec_type"] == "video"), {})
    n, _, m = v.get("r_frame_rate", "0/1").partition("/")
    return float(d["format"]["duration"]), v.get("width"), v.get("height"), float(n) / float(m or 1), \
        any(s["codec_type"] == "audio" for s in d["streams"])
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
    i, p = re.findall(r"I: (-?[\d.]+) LUFS", err), re.findall(r"Peak: (-?[\d.]+) dBFS", err)
    return (float(i[-1]) if i else None), (float(p[-1]) if p else None)
def cortes(video):
    err = ff(video, "-an", "-vf", "select='gt(scene,0.35)',showinfo")
    return [float(x) for x in re.findall(r"pts_time:([\d.]+)", err)]
def palavras(texto):
    return [NUM.get(w, w) for w in re.findall(r"[\w']+", texto.lower())]
def plantar_erro(video, dur, pasta):
    # sonda: copia 10 s do meio do video com 1,5 s de tela preta e silencio plantados em 5 s
    sonda, ini = pasta / "sonda.mp4", max(dur / 2 - 5, 0)
    rodar(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-ss", f"{ini:.2f}", "-t", "10", "-i", str(video),
           "-vf", "drawbox=enable='between(t,5,6.5)':color=black:t=fill", "-af", "volume=enable='between(t,5,6.5)':volume=0",
           "-c:v", "libx264", "-preset", "ultrafast", "-c:a", "aac", str(sonda)])
    return sonda
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("--roteiro"); ap.add_argument("--ouvido")
    ap.add_argument("--formato", help="ex.: 1080x1920"); ap.add_argument("--pausa", type=float, default=0.6)
    ap.add_argument("--saida", default="conferencia"); ap.add_argument("--sonda", action="store_true")
    a = ap.parse_args()
    video, out = Path(a.video), Path(a.saida)
    shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    falhas, avisos, rel = [], [], [f"# Conferencia de {video.name}", ""]
    dur, w, h, fps, tem_audio = info(video)
    imagem = f"{w}x{h}, {fps:.2f} quadros por segundo" if w else "sem imagem"
    rel += ["## Arquivo", f"{dur:.2f} s, {imagem}, audio: {'sim' if tem_audio else 'NAO'}", ""]

--- PAGE 4 ---
    if a.formato and f"{w}x{h}" != a.formato: falhas.append(f"formato {w}x{h}, o pedido era {a.formato}")
    if w and h and abs(w / h - 9 / 16) > 0.01: avisos.append(f"proporcao {w}x{h} nao e 9:16")
    if not tem_audio: falhas.append("o video nao tem audio")
    if tem_audio:
        sil = silencios(video, dur)
        comeco = next((b for x, b in sil if x <= 0.01), 0.0)
        final = next((dur - x for x, b in sil if b >= dur - 0.01), 0.0)
        internas = [(x, b) for x, b in sil if x > 0.01 and b < dur - 0.01 and b - x > a.pausa]
        rel += ["## Fala, comeco e fim", f"Primeira fala em {comeco:.2f} s. Depois da ultima fala sobram {final:.2f} s.",
                f"Pausas acima de {a.pausa} s no meio: {len(internas)}"]
        rel += [f"- {x:.2f} s a {b:.2f} s ({b - x:.2f} s de silencio)" for x, b in internas] + [""]
        if comeco > 0.5: falhas.append(f"a fala so comeca em {comeco:.2f} s")
        if final > 1.2: falhas.append(f"sobram {final:.2f} s de silencio no fim")
        if final < 0.08: avisos.append("o audio termina colado na ultima fala: confira se a ultima palavra saiu inteira")
        falhas += [f"espaco demais: {b - x:.2f} s de silencio em {x:.2f} s" for x, b in internas]
        lufs, pico = volume(video)
        rel += ["## Volume", f"Integrado: {lufs} LUFS. Pico: {pico} dBFS.", ""]
        if lufs is not None and not -16 <= lufs <= -12: avisos.append(f"volume integrado em {lufs} LUFS, fora da faixa de -16 a -12")
        if pico is not None and pico > -1: avisos.append(f"pico em {pico} dBFS, acima de -1")
    pr = [(x, b) for x, b in pretos(video) if x > 0.05 and b < dur - 0.05]
    falhas += [f"tela preta de {b - x:.2f} s em {x:.2f} s" for x, b in pr]
    avisos += [f"imagem parada por 2 s ou mais a partir de {x:.2f} s" for x in congelados(video)]
    cs = cortes(video)
    rel += ["## Cortes", f"{len(cs)} cortes de imagem. Cada corte_NN.jpg mostra 0,2 s antes a esquerda e 0,2 s depois a direita."]
    for i, t in enumerate(cs, 1):
        rel.append(f"- corte {i:02d}: {t:.2f} s")
        rodar(["ffmpeg", "-nostdin", "-loglevel", "error", "-ss", f"{max(t - 0.2, 0):.2f}", "-i", str(video), "-ss", f"{t + 0.2:.2f}",
               "-i", str(video), "-filter_complex", "[0:v]scale=360:-2[a];[1:v]scale=360:-2[b];[a][b]hstack", "-frames:v", "1",
               "-q:v", "4", str(out / f"corte_{i:02d}.jpg")])
    rodar(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", str(video), "-vf", "fps=1/2,scale=270:-2,tile=4x3", "-q:v", "4",
           str(out / "folha_%02d.jpg")])
    rel += ["", "## Folhas de quadros", "1 quadro a cada 2 s, 12 por folha, da esquerda pra direita e de cima pra baixo: "
            "a folha_01 vai de 0 a 22 s, a folha_02 de 24 a 46 s, e assim por diante.", ""]
    if a.roteiro and a.ouvido:
        e, o = palavras(Path(a.roteiro).read_text()), palavras(Path(a.ouvido).read_text())
        dif = [(op, " ".join(e[i1:i2]), " ".join(o[j1:j2])) for op, i1, i2, j1, j2 in
               difflib.SequenceMatcher(a=e, b=o, autojunk=False).get_opcodes() if op != "equal"]
        rel += ["## Roteiro contra o que se ouve", f"Esperadas {len(e)} palavras, ouvidas {len(o)}. Diferencas: {len(dif)}"]
        nome = {"replace": "trocou", "delete": "faltou", "insert": "sobrou"}
        rel += [f"- {nome[op]}: esperado '{x}', ouvido '{y}'" for op, x, y in dif] + [""]
        falhas += [f"fala diferente do roteiro: esperado '{x}', ouvido '{y}'" for op, x, y in dif]
    if a.sonda:
        with tempfile.TemporaryDirectory() as tmp:
            s = plantar_erro(video, dur, Path(tmp))
            pegou_preto = any(4.8 <= x <= 5.2 for x, b in pretos(s))
            pegou_som = any(4.8 <= x <= 5.2 and b - x > a.pausa for x, b in silencios(s, 10.0)) if tem_audio else True
        ok = pegou_preto and pegou_som
        rel += ["## Sonda", f"Erro plantado (1,5 s de tela preta e silencio): {'pego' if ok else 'NAO foi pego'}", ""]
        if not ok: falhas.append("a sonda com erro plantado passou sem ser pega: a conferencia esta cega")
    rel += ["## Avisos"] + [f"- {x}" for x in avisos] + ["", "## Veredito"]
    rel += ["APROVADO"] if not falhas else ["CONSERTAR"] + [f"- {x}" for x in falhas]
    (out / "RELATORIO.md").write_text("\n".join(rel) + "\n")
    print("\n".join(rel))
    sys.exit(1 if falhas else 0)
if __name__ == "__main__":
    main()
PY
# confere o render, com a sonda que planta um erro pra provar que ele enxerga
python3 conferir_video.py render/final.mp4 --formato 1080x1920 --sonda  Atalho: Com musica por baixo, a pausa some na medicao,
porque a trilha preenche o silencio: no video de teste de 92 s, com musica, ele achou 0 pausas. Confira a pausa na voz antes da
mixagem, rodando o mesmo script no arquivo de audio so da voz.  https://formulae.brew.sh/formula/ffmpeg

--- PAGE 5 ---
8. Teste o conferidor com um erro plantado
Conferencia que nunca reprova nao esta conferindo nada, entao antes de confiar nela, plante um erro e veja se ela pega. O --sonda faz
isso sozinho: copia 10 s do meio do video com 1,5 s de tela preta e silencio e confere a copia, e se o erro passar, o veredito vira
CONSERTAR com o aviso de que a conferencia esta cega. No teste de 7 de novembro, num trecho de 12 s com 5 erros plantados a
mao, ele pegou os 5.  1) Os 5 do teste: o formato 720x1280 no lugar de 1080x1920, a fala comecando em 0,81 s, 1,30 s de silencio em
4,02 s, 0,43 s de tela preta em 8,00 s e a palavra comment trocada por come and na transcricao  2) O mesmo trecho sem os erros, em
1080x1920, saiu APROVADO  3) Achou na mao um erro que a conferencia deixou passar: ele vira checagem nova no script e um erro
plantado novo, com o prompt 10  # cria uma copia de 12 s com 3 erros: 0,8 s mudo no comeco, 1,3 s de silencio no meio e 0,4 s de tela
preta
ffmpeg -y -t 12 -i render/final.mp4 \
  -vf "drawbox=enable='between(t,8,8.4)':color=black:t=fill" \
  -af "volume=enable='between(t,0,0.8)+between(t,4,5.3)':volume=0" \
  -c:v libx264 -c:a aac teste-com-erro.mp4
# tem que sair CONSERTAR, com os 3 erros na lista, e a sonda pega
python3 conferir_video.py teste-com-erro.mp4 --saida conferencia-teste --sonda
9. Ligue o conferidor num Stop hook da pasta de edicao
Com o hook, o Claude nao consegue encerrar a vez com o render reprovado: toda vez que ele tenta parar, o script pega o MP4 mais
novo da pasta render, roda a conferencia e, se reprovar, devolve o veredito com codigo 2 e ele volta pra consertar. Se a pasta tem
roteiro.txt, o hook tambem exige a transcricao do render novo em ouvido.txt antes de deixar terminar. Ele rodou em 7 de novembro nos
7 casos: sem render, render ruim, render bom, roteiro sem transcricao, palavra trocada, transcricao batendo e render ja aprovado.  1) O
hook usa a forma com args, que a documentacao recomenda quando o caminho usa a variavel CLAUDE_PROJECT_DIR, porque ela
aguenta pasta com espaco no nome  2) Render aprovado ganha o arquivo conferencia/APROVADO, e o hook nao confere de novo
enquanto nao sair um MP4 mais novo  3) O timeout de 600 s e o padrao do hook de comando, e a conferencia do video de 92 s levou
30 s  4) Se o .claude/settings.json ja existe, peca pro Claude juntar o bloco hooks em vez de sobrescrever o arquivo  # na pasta do
projeto de edicao, com o conferir_video.py na raiz
mkdir -p .claude/hooks
cat > .claude/hooks/conferir-video.sh <<'SH'
#!/bin/bash
# Stop hook: o Claude so termina quando o render mais novo passa na conferencia
cd "$CLAUDE_PROJECT_DIR" || exit 0
VIDEO=$(ls -t render/*.mp4 2>/dev/null | head -1)
[ -z "$VIDEO" ] && exit 0
[ -f conferencia/APROVADO ] && [ conferencia/APROVADO -nt "$VIDEO" ] && exit 0
EXTRA=""
if [ -f roteiro.txt ]; then
  if [ ! -f ouvido.txt ] || [ ouvido.txt -ot "$VIDEO" ]; then
    echo "Transcreva o render $VIDEO em ouvido.txt antes de terminar, pra conferencia comparar com o roteiro.txt." >&2
    exit 2
  fi
  EXTRA="--roteiro roteiro.txt --ouvido ouvido.txt"
fi
if python3 conferir_video.py "$VIDEO" --formato 1080x1920 $EXTRA > .claude/ultima-conferencia.txt 2>&1; then
  touch conferencia/APROVADO; exit 0
fi
tail -25 .claude/ultima-conferencia.txt >&2
echo "O render $VIDEO nao passou na conferencia. Leia conferencia/RELATORIO.md, abra as folhas e os cortes, conserte e renderize
de novo." >&2
exit 2
SH
chmod +x .claude/hooks/conferir-video.sh
# liga o hook no projeto
cat > .claude/settings.json <<'JSON'
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "bash", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/conferir-video.sh"], "timeout": 600 }
        ]
      }
    ]
  }
}
JSON  Atalho: O teto de 8 continuacoes seguidas conta so quando o Claude tenta parar sem usar ferramenta no meio. Renderizar de
novo zera a conta, entao o ciclo de consertar e renderizar segue ate aprovar.  https://code.claude.com/docs/en/hooks

--- PAGE 6 ---
10. Ponha um revisor que nao escreveu o trabalho
Quem escreveu o codigo carrega o raciocinio que usou, e um revisor que nao viu a conversa nao tem esse vies. O /code-review revisa
as mudancas da sua branch e funciona em qualquer plano, e pra revisar contra a sua especificacao, ou revisar o que nao e codigo,
como a legenda ou o anuncio, voce cria um subagente revisor so com as ferramentas de leitura.  1) Peca assim: use o subagente
revisor pra conferir o que foi feito contra o SPEC.md  2) A documentacao manda manter o ignore estilo no pedido, porque um revisor
pedido pra achar problema sempre acha alguma coisa, e consertar tudo enche o projeto de camada e teste inutil  3) Uma segunda
sessao do Claude Code tambem serve de revisor, ja que ela le o arquivo sem ter visto ele ser escrito  # o revisor pronto do Claude
Code: revisa a branch num subagente que nao viu a conversa
/code-review
# um revisor de fora, so com ferramentas de leitura, pra qualquer entrega
mkdir -p .claude/agents
cat > .claude/agents/revisor.md <<'MD'
---
name: revisor
description: Revisa uma entrega contra a especificacao e a regua do projeto, sem ter visto como ela foi feita. Use antes de dizer que
terminou.
tools: Read, Glob, Grep
---
Voce e o revisor. Leia a especificacao ou a regua que te passarem e confira a entrega item por item.
Para cada item, responda passou ou falhou, com o trecho ou o arquivo que prova.
Aponte so o que afeta o resultado e ignore preferencia de estilo.
Termine com APROVADO ou CONSERTAR e a lista do que falta.
MD  https://code.claude.com/docs/en/sub-agents
11. Deixe rodar sozinho, com limite e com alguem aprovando no fim
Com o loop fechado, o Claude leva a tarefa ate o fim sem voce, e e isso que o Boris descreve quando diz que nao fala mais com um
agente, fala com um loop ou com uma rotina que faz os prompts por ele. Antes de soltar, a documentacao pede 5 respostas: o que e
pronto, como ele confere, o que pode mexer, o que faz ele parar e quem aprova o resultado. O comando abaixo roda um pedido por
video, com teto de voltas e de gasto.  1) O --max-turns encerra a chamada com erro quando passa do teto, e o --max-budget-usd para
quando o gasto estimado chega no valor  2) O /loop repete um prompt num intervalo enquanto a sessao esta aberta, e o /schedule cria
uma tarefa agendada na nuvem, que roda com o notebook fechado  3) O que nao volta atras, como publicar, subir campanha, agendar
post ou fazer deploy, fica com uma pessoa aprovando  # um pedido por video da pasta brutos, cada um com teto de 30 voltas e de US$
3 de gasto estimado
for v in brutos/*.mp4; do
  claude -p "/goal edite $v seguindo o CLAUDE.md, renderize em render/ e rode a conferencia ate o relatorio terminar em APROVADO,
ou pare depois de 8 voltas" \
    --permission-mode auto --max-turns 30 --max-budget-usd 3
done
# dentro de uma sessao aberta: repete a checagem a cada 15 minutos
/loop 15m confira o CI desta branch e, se estiver vermelho, leia o log, conserte e suba  https://code.claude.com/docs/en/headless
Os 4 jeitos de fechar o loop, e quem decide em cada um
Da documentacao oficial do Claude Code, conferida em 7 de novembro de 2026 na versao 2.1.319. Quanto mais pra
baixo na lista, menos o resultado depende do modelo lembrar.
1. No pedido
Voce diz o que conta como pronto e pede a prova, como rodar os testes no fim e continuar ate passarem. Funciona hoje em qualquer
tarefa, sem configurar nada.
2. O /goal
Um modelo separado le a conversa depois de cada volta e manda continuar ate a condicao valer. Pesa mais em tarefa longa, quando o
Claude as vezes fecha a vez com um resumo e ainda tem item aberto.
3. O Stop hook
O seu comando roda toda vez que o Claude tenta parar, e o codigo 2 manda ele de volta. A vez nao termina enquanto a checagem
falha, ate o teto de 8 continuacoes seguidas.
4. O revisor de fora
O /code-review, um subagente revisor ou uma segunda sessao leem o resultado sem ter visto o raciocinio que produziu ele.
5. O /verify, junto com qualquer um
Compila, abre e usa o app pra ver se a mudanca funciona, e pega o que o teste e a checagem de tipo deixam passar.

--- PAGE 7 ---
O loop em cada trabalho: a checagem que volta passou ou falhou
Pra engenharia, programacao, trafego pago e copywriting, e tambem pra edicao de video e site: o que da olhos pro
Claude em cada trabalho e o que ele confere antes de dizer que terminou.
Edicao de video
O comeco, as pausas, o fim, a tela preta, o volume e o roteiro contra o que se ouve, pelo script, e a legenda em cima do rosto e o corte
no lugar errado, pelas folhas de quadros que ele abre como imagem.
Programacao
O teste que reproduz o bug falhando antes e passando depois, o build saindo com 0 e o typecheck limpo, travados num Stop hook.
Engenharia de produto
O app aberto e usado de verdade, com o print do navegador ao lado do mockup, o console sem erro e o fluxo principal clicado ate o fim.
Trafego pago
Antes de subir, a soma do orcamento diario bate com o combinado, nenhum conjunto passa do teto, todo link tem UTM e o nome segue
o padrao, tudo conferido na planilha exportada do gerenciador. Subir a campanha fica com voce.
Copywriting
Cada regra da marca vira um item que passa ou falha, como a primeira linha, o tamanho, a palavra proibida e o CTA, conferidos um por
um com o trecho que prova.
Relatorio e planilha
Cada total recalculado a partir da base original e cada numero do texto achado na planilha, com a celula de onde ele saiu.
QA
Os passos do roteiro de teste executados na ordem, com o print de cada um e o resultado esperado ao lado do que apareceu.
O que o conferidor de video confere e como
Cada checagem do conferir_video.py, com o filtro do ffmpeg que mede e o limite que reprova, rodado em 7 de novembro
de 2026 no ffmpeg 9.0.2.
Formato
Largura, altura, quadros por segundo e se tem audio. Reprova quando o tamanho nao e o do --formato e avisa quando a proporcao nao
e 9:16.
Comeco da fala
O silencio abaixo de -35 dB no comeco, que reprova quando a fala so comeca depois de 0,5 s.
Pausas no meio
Todo silencio maior que o --pausa, de 0,6 s por padrao, vira uma linha com o segundo em que acontece: e o espaco demais de um lado.
Fim
Reprova quando sobra mais de 1,2 s de silencio depois da ultima fala e avisa quando o audio acaba colado nela, que e quando a ultima
palavra pode ter sido cortada.
Tela preta
Qualquer trecho preto de 0,1 s ou mais fora do comeco e do fim reprova.
Imagem parada
Avisa quando a imagem fica igual por 2 s ou mais, sem reprovar, porque uma cartela parada pode ser de proposito.
Volume
O volume integrado em LUFS e o pico, com aviso fora da faixa de -16 a -12 LUFS ou com pico acima de -1 dBFS.
Cortes
Cada troca brusca de imagem vira um corte_NN.jpg com o quadro de 0,2 s antes e o de 0,2 s depois, pro Claude ver se cortou no lugar
certo.
Roteiro contra o que se ouve
Compara palavra por palavra o roteiro.txt com a transcricao do render e lista o que trocou, o que faltou e o que sobrou.

--- PAGE 8 ---
Sonda
Planta 1,5 s de tela preta e silencio numa copia de 10 s e confere se a conferencia pega. Se nao pegar, reprova tudo.
O que o criador do Claude Code diz sobre verificacao, com a fonte
As frases do Boris Cherny, que criou e chefia o Claude Code, no lugar e na data em que foram ditas. Traducao nossa,
com o original na nota.
1. A dica mais importante
Provavelmente o mais importante pra ter otimos resultados no Claude Code e dar a ele um jeito de verificar o proprio trabalho: com esse
loop de retorno, a qualidade do resultado final fica 2 a 3 vezes maior. Ele completa que a verificacao muda em cada area, de um
comando no terminal ou uma bateria de testes ao app testado no navegador ou no simulador do celular.  Atencao: Original: give Claude
a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result. 
https://x.com/bcherny/status/2007179861115511237
2. Tarefa muito longa
Em tarefa muito longa, ele pede pro Claude verificar o trabalho com um agente em segundo plano no fim, usa um Stop hook de agente
pra fazer isso de um jeito mais garantido ou usa o plugin do Ralph, que hoje esta no marketplace oficial como ralph-loop.  Atencao:
Original: prompt Claude to verify its work with a background agent when it's done, use an agent Stop hook to do that more
deterministically, or use the ralph-wiggum plugin.  https://x.com/bcherny/status/2007179858435281082
3. Falar com um loop
O salto de agora, segundo ele, e nao falar mais com um agente: ele fala com um loop ou com uma rotina, e ela faz os prompts pro
Claude por ele. A frase esta em Reflecting on a year of Claude Code, a conversa dele com a Cat Wu no canal do Claude.  Atencao:
Original: I don't talk to an agent anymore. I talk to loop or I talk to a routine and it prompts Claude for me. 
https://www.youtube.com/watch?v=Hth_tLaC2j8&t=653s
4. O que mais gente erra
Na conversa da Y Combinator, ele diz que a habilidade agora e dar uma tarefa um pouco dificil demais e um jeito do Claude verificar o
proprio trabalho. O exemplo dele e reescrever o app de desktop do Claude comparando print pixel por pixel, numa tarefa que rodava
havia mais de 2 semanas.  https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1172s
Os comandos e arquivos do loop
Todos existem no Claude Code 2.1.319, de 6 de novembro de 2026.
/goal
Poe a condicao de pronto com o juiz separado. O /goal sozinho mostra o andamento e o /goal clear tira a meta.  INSTALL: /goal o
relatorio termina em APROVADO, ou pare depois de 8 voltas
/verify
Compila, roda e usa o app pra confirmar a mudanca, e grava a receita em .claude/skills/verify/SKILL.md.  INSTALL: /verify
/run-skill-generator
Sobe o projeto do zero e grava como, pro /run, o /verify e qualquer agente seguirem a mesma receita.  INSTALL: /run-skill-generator
/code-review
Revisa as mudancas da branch atras de bug, em qualquer plano. O /review e o mesmo comando.  INSTALL: /code-review
/hooks
Mostra os hooks que carregaram, os do projeto e os seus.  INSTALL: /hooks
claude --chrome
Abre a sessao ligada ao seu navegador, pro Claude testar a pagina, ler o console e tirar print.  INSTALL: claude --chrome
/loop
Repete o prompt no intervalo enquanto a sessao esta aberta, e sem intervalo o Claude escolhe o ritmo.  INSTALL: /loop 15m confira o
CI e conserte o que quebrou
claude -p
Roda um pedido sem abrir a conversa, que e como o loop entra em script, em CI e em lote.  INSTALL: claude -p "/goal o teste passa"
--max-turns 30

--- PAGE 9 ---
.claude/settings.json
Onde mora o Stop hook do projeto, que vale pra todo mundo que abrir a pasta depois de confiar nela.
10 prompts pra fechar o loop
O 1 serve pra qualquer tarefa, do 2 ao 4 sao da edicao de video, o 5 e o 6 gravam e revisam a conferencia, do 7 ao 9
sao pra copy, trafego pago e site, e o 10 faz a conferencia aprender com o erro que passou. Troque o que esta entre
colchetes.
1. 1. O pedido com prova
Objetivo: [o que tem que estar pronto, ex.: o formulario de cadastro valida o e-mail e mostra o erro em portugues].
Como provar que esta pronto:
1. [ex.: npm test sai com 0 e o teste novo do formulario passa]
2. [ex.: voce sobe o app, preenche um e-mail invalido e me mostra o print da mensagem]
Restricoes: [ex.: nao mexa no banco e nao instale biblioteca nova].
Rode a checagem no fim e continue ate ela passar. Quando terminar, me mostre o comando que rodou e a saida, ou o print. Se travar
no mesmo ponto 3 vezes, pare e me explique o que tentou.
2. 2. A edicao de video que se confere
Edite [arquivo do bruto] seguindo o roteiro em roteiro.txt e renderize em render/final.mp4, em 1080x1920.
Depois de cada render:
1. Transcreva o render em ouvido.txt com [a ferramenta de transcricao que voce usa]
2. Rode python3 conferir_video.py render/final.mp4 --formato 1080x1920 --roteiro roteiro.txt --ouvido ouvido.txt
3. Abra cada conferencia/folha_*.jpg e cada conferencia/corte_*.jpg e descreva o que viu em cada imagem
4. Conserte tudo que o relatorio e as imagens mostraram e renderize de novo
So diga que terminou quando o relatorio terminar em APROVADO e voce tiver descrito todas as imagens. No fim, me mostre o
RELATORIO.md e a lista do que consertou.
3. 3. A meta da edicao com /goal
/goal o RELATORIO.md do render mais novo em render/ termina em APROVADO e aparece colado na conversa, e voce descreveu
cada folha e cada corte da pasta conferencia, sem mexer no roteiro.txt, ou pare depois de 8 voltas
4. 4. Olhar as folhas de quadros
Abra todas as imagens da pasta conferencia: as folha_*.jpg tem 12 quadros cada, 1 a cada 2 segundos, da esquerda pra direita e de
cima pra baixo, e as corte_*.jpg mostram 0,2 s antes e 0,2 s depois de cada corte.
Para cada imagem, me diga:
1. Se a legenda ou algum texto cobre o rosto, a boca ou os olhos
2. Se algum texto esta cortado na borda ou perto demais do topo e da base, onde a interface do Instagram cobre
3. Se o corte caiu no meio de um gesto ou com a boca aberta no meio de uma palavra
4. Se alguma animacao aparece por cima de outra ou deixa o texto ilegivel
5. Se a cor ou o enquadramento muda de um quadro pro outro sem motivo
Monte uma tabela com a imagem, o segundo aproximado, o problema e o conserto. Se a imagem estiver certa, escreva ok.
5. 5. A skill de conferencia do projeto
Crie a skill .claude/skills/conferir-entrega/SKILL.md deste projeto, em portugues do Brasil, com no maximo 60 linhas:
1. No frontmatter, name conferir-entrega e uma description que diga pra usar antes de dizer que qualquer entrega terminou
2. Os comandos exatos de conferencia deste projeto, na ordem, cada um com o que conta como passou
3. O que abrir e olhar alem dos comandos: prints, folhas de quadros, a pagina no navegador
4. O formato da prova que voce me mostra no fim: comando, saida e veredito
5. Uma secao de armadilhas, com os erros que ja passaram sem ser pegos
Depois rode a skill uma vez agora, de verdade, e me mostre o resultado.
6. 6. A revisao contra a especificacao
Use um subagente pra revisar o que foi feito contra o SPEC.md. Confira se cada requisito foi implementado e se os casos de borda
listados tem teste. Relate so as falhas que afetam o funcionamento e ignore estilo.
7. 7. A regua da copy
Antes de me entregar o texto, confira cada regra abaixo e monte uma tabela com a regra, passou ou falhou e o trecho que prova:

--- PAGE 10 ---
1. A primeira linha e uma promessa ou um numero
2. Tem no maximo [N] caracteres
3. Nenhuma destas palavras aparece: [palavras proibidas da marca]
4. O CTA pede [a acao, ex.: comentar o codigo da legenda]
5. Todo numero tem a fonte em [onde a fonte fica]
6. [outra regra da sua marca]
Se alguma falhar, reescreva e confira de novo. So me entregue quando todas passarem, com a tabela no fim.
8. 8. A campanha conferida antes de subir
Abaixo esta a planilha exportada do gerenciador de anuncios com a campanha montada. Antes de eu subir, confira:
1. A soma do orcamento diario de todos os conjuntos e R$ [valor combinado]
2. Nenhum conjunto passa de R$ [teto por conjunto]
3. Todo link de destino tem utm_source, utm_medium e utm_campaign
4. O nome de cada campanha, conjunto e anuncio segue o padrao [padrao de nome]
5. O publico e a regiao de cada conjunto sao [o combinado]
Monte uma tabela com cada item, passou ou falhou e a linha da planilha. Nao suba nada, a publicacao fica comigo.
PLANILHA:
[cole aqui]
9. 9. A landing page conferida no navegador
Abra [endereco local da pagina, ex.: localhost:3000] no Chrome em 390 px e em 1440 px de largura.
1. Tire print das 2 larguras e compare com o mockup em [arquivo do mockup]
2. Confira se o console esta sem erro e se nenhum pedido de rede falhou
3. Clique no botao principal e preencha o formulario com dados de teste ate a tela de obrigado
4. Liste cada diferenca com o mockup e cada erro, conserte e confira de novo
So diga que terminou quando as 2 larguras baterem com o mockup e o fluxo chegar ate o fim, e me mostre os prints finais.
10. 10. O erro que passou vira checagem nova
Eu achei este erro na entrega e a conferencia deixou passar: [descreva o erro, ex.: a legenda cobriu o rosto entre 12 e 14 segundos].
1. Explique em 1 frase por que a conferencia nao pegou
2. Acrescente uma checagem nova que pegue esse tipo de erro, no script ou na skill de conferencia
3. Plante esse mesmo erro numa copia de teste e mostre que agora a conferencia reprova
4. Rode de novo na entrega boa e mostre que ela continua aprovada
5. Registre a regra nova no CLAUDE.md, na secao Como provar que ficou pronto
Antes de deixar o Claude trabalhar sem voce
As 7 conferencias, da checagem ao aprovado final.
Existe uma checagem que volta passou ou falhou, e o comando dela esta no CLAUDE.md  |  A checagem reprovou um
erro plantado de proposito antes de voce confiar nela  |  O Claude mostra a prova no fim: o comando, a saida, o relatorio
ou o print  |  Tem limite: o numero de voltas na condicao do /goal, o --max-turns ou o teto do Stop hook  |  Alguem que
nao fez o trabalho revisou, seja o /code-review, o subagente revisor ou uma segunda sessao  |  O que nao volta atras,
como publicar, subir campanha, agendar post ou fazer deploy, passa por uma pessoa  |  Cada erro que voce achou na
mao virou uma checagem nova
Funciona no Brasil?
Funciona no Brasil do mesmo jeito: o Claude Code entende e responde em portugues, e o /goal, o Stop hook, o /verify, o
Superpowers, o ffmpeg e o conferidor desta pagina sao gratis. O unico custo e o Claude Code, que vem a partir do
Claude Pro, R$ 110 por mes ou R$ 92 no anual, cobrado em real, e as frases do Boris estao em ingles, no X e no
YouTube, que gera a legenda em portugues nas configuracoes do video.
Links
A dica 13 do Boris Cherny: https://x.com/bcherny/status/2007179861115511237  |  Boas praticas do Claude Code:
https://code.claude.com/docs/en/best-practices  |  O /goal: https://code.claude.com/docs/en/goal  |  Guia de hooks:
https://code.claude.com/docs/en/hooks-guide  |  Referencia de hooks: https://code.claude.com/docs/en/hooks  |  Skills do

--- PAGE 11 ---
Claude Code: https://code.claude.com/docs/en/skills  |  O Claude no Chrome: https://code.claude.com/docs/en/chrome  | 
Superpowers: https://github.com/obra/superpowers  |  Reflecting on a year of Claude Code:
https://www.youtube.com/watch?v=Hth_tLaC2j8  |  O ffmpeg no Mac: https://formulae.brew.sh/formula/ffmpeg
Dica do Fabiano
Comeca pelo trabalho que voce mais corrige na mao, porque e ali que o loop se paga primeiro: escreve a checagem que
volta passou ou falhou, planta um erro de proposito pra ver se ela pega e so depois deixa o Claude rodar sozinho. E todo
erro que escapar e voce achar no olho vira uma checagem nova, assim a conferencia fica mais esperta a cada entrega e
voce sai do papel de gargalo.
fabiano.app