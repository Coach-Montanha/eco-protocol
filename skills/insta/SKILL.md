---
name: insta
description: Hub mestre audiovisual para Instagram: vídeos verticais 9:16, carrosséis, roteiros de stories e legendas.
---

# 🎬 /insta — Hub Mestre Audiovisual & Editorial (@insta)

O `/insta` (ou `@insta`) é o comando mestre definitivo para toda a esteira de conteúdo visual, produção de vídeos verticais (9:16) e pacotes editoriais do Ecossistema Montanha. Ele funde captação, edição local FFmpeg, narração neural, legendas dinâmicas e roteirização.

---

## 1. Pacote Editorial Instagram Completo
Sempre que acionado, entrega o kit completo de publicação:
1. **Carrossel 1:1 de Alta Conversão**: 8 a 10 slides estruturados com gancho, desenvolvimento visual e chamada final.
2. **Legenda Magnética**: Copy persuasiva com primeira linha de impacto, espaçamento limpo, quebra de objeções e hashtags estratégicas.
3. **Roteiro de Stories Interativos**: Sequência de 3 a 5 stories (caixa de perguntas sem filtro, bastidores, enquete e CTA).
4. **Copy Multiplataforma**: Adaptações diretas para Reels, Shorts, TikTok e LinkedIn.

---

## 2. Dual Real Video Engine (9:16 — 1080x1920)

### Opção A — Vídeo Neural Generativo (`/insta video neural`)
* Aciona o modelo generativo (`gemini-omni-1.1-flash` / Higgsfield Effects) para animar fotos em alta resolução ou gerar cenas 3D por prompt.
* Renderização cinematográfica em 4K com física realista de tecidos, músculos, suor e iluminação volumétrica (10s a 40s).

### Opção B — Vídeo B-Roll Narrado (`/insta video broll`)
* Pipeline local acelerado com FFmpeg:
  1. **Download de Mídias (`cobalt`)**: Captura rápida de referências ou clipes sem marcas d'água.
  2. **Análise & Transcrição (`video-understand`)**: Transcrição Whisper local e extração de frames-chave sem gastar tokens.
  3. **Edição Cirúrgica (`video-edit`)**: Cortes precisos, concatenação, crop para 1080x1920 e normalização de áudio.
  4. **Narração Neural Brasileira (`pixelle-video`)**: Voz ultra-realista calibrada para o tom do Coach Montanha.
  5. **Legendas Dinâmicas Animadas (`pixelle-video` / `motion-skills`)**: Arquivos `.ass` com destaque de palavras faladas em tempo real e transições fluidas.
  6. **Design Acústico & Sincronia (`earshot-audio` / `rhubarb-lip-sync`)**: Efeitos sonoros (SFX), trilha de fundo com ducking e sincronização labial quando houver avatar.

---

## 3. Modificadores Fotográficos & Iluminação de Estúdio
- `/gymNewBg`: Cenário de academia de alta performance com halteres e iluminação ambiente.
- `/3pointsLighting`: Iluminação de estúdio profissional 3 pontos (Key, Fill, Rim/Backlight).
- `/removePeopleBg`: Isola o elemento/atleta principal removendo pessoas ao fundo.
- `/volumetricLighting`: Raios de luz volumétrica e atmosfera dramática de névoa.
- `/cinematicBokehLighting`: Desfoco cinematográfico com abertura f/1.4 e círculos de bokeh.
- `/editorial`: Estética de catálogo esportivo e revista de fitness de elite.

---

## 4. Aliases Integrados
Os seguintes comandos satélites são atendidos nativamente pelo `/insta`:
- `/video-studio`, `/video-edit`, `/video-understand`, `/pixelle-video`, `/cobalt`, `/producao-video-hypit`, `/brag`.
