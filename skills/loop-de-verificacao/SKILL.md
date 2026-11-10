---
name: loop-de-verificacao
description: Implementa o loop fechado de verificação autônoma baseado na metodologia de Boris Cherny (criador do Claude Code) e Fabiano. Garante que o agente confira o próprio trabalho antes de declarar conclusão via Stop hooks, pedidos com prova, sondas com erros plantados, revisores cegos e scripts de auditoria (código, vídeo, copy, tráfego e web).
---

# Loop de Verificação Autônoma (Verification Loop)

> "Provavelmente o mais importante pra ter ótimos resultados é dar ao modelo um jeito de verificar o próprio trabalho: com esse loop de retorno, a qualidade do resultado final fica de 2 a 3 vezes maior."  
> — **Boris Cherny**, criador e líder do Claude Code na Anthropic.

O **Loop de Verificação** resolve o maior problema de agentes de IA: **o agente para quando o trabalho *parece* pronto**. Sem uma checagem determinística que retorne `passou` ou `falhou`, o usuário humano vira o gargalo de testes manuais a cada iteração.

Esta skill fornece a infraestrutura completa para transformar agentes em operadores de loop fechado: do pedido com prova até **Stop Hooks** à prova de falhas com código de saída 2, testes de sonda com erros plantados, revisores cegos independentes e scripts de auditoria multimodal (áudio, vídeo, código e copy).

---

## 🏗️ Os 4 Níveis de Fechamento de Loop

```
┌────────────────────────────────────────────────────────────────────────┐
│ Nível 1: Pedido com Prova (Prompting Defensivo)                        │
│ -> Exige comando + saída de teste no prompt, nunca apenas "terminei"   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Nível 2: Meta Fechada (/goal)                                          │
│ -> Juiz externo avalia se a condição de término foi atingida na tela   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Nível 3: Stop Hook Determinístico (.claude/settings.json)              │
│ -> Intercepta a saída da sessão. Se falhar, sai com código 2 e barra!  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Nível 4: Revisor Cego Independente (Subagente sem viés)                │
│ -> Modelo sem acesso à conversa audita a entrega contra a especificação│
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Os 11 Passos de Implementação

### 1. Documentar a Prova no `CLAUDE.md`
A linha mais importante da configuração do projeto é o comando exato que prova que o trabalho funciona:
```markdown
## Como provar que ficou pronto
- Código: npm test e npm run build, ambos saindo com 0
- Vídeo: python scripts/conferir_video.py render/final.mp4 --formato 1080x1920 --sonda (terminando em APROVADO)
- Copy e Anúncios: Régua em regras-copy.md atendida item por item com trecho comprovando
- Regra: Antes de encerrar, execute a checagem e mostre a saída completa.
```

### 2. Pedir a Prova, Nunca um "Terminei"
Não aceite frases como "todos os testes passaram" sem evidência. O prompt deve exigir o comando rodado e a saída:
```markdown
Objetivo: Validar formulário de e-mail e exibir erro em vermelho.
Como provar: Execute npm test. Mostre o comando, a saída com código 0 e o print da mensagem de erro.
```

### 3. Loop com Juiz Externo (`/goal`)
Use o comando `/goal` para acionar um modelo avaliador separado que examina a conversa após cada iteração:
```bash
/goal npm test sai com 0, o lint está limpo e nenhum outro arquivo de teste mudou, ou pare após 15 voltas
```

### 4. Stop Hook Travado no Código 2 (Sem Exceção)
O **Stop Hook** é executado toda vez que o agente tenta encerrar sua vez.  
- **Código 0**: O agente tem permissão para encerrar.
- **Código 2**: A finalização é cancelada e a mensagem impressa no `stderr` é injetada como a próxima instrução obrigatória para o agente consertar.

Configuração em `.claude/settings.json`:
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "npm test 1>&2 || exit 2", "timeout": 300 }
        ]
      }
    ]
  }
}
```

### 5. O Princípio da Sonda: Erro Plantado de Propósito
> **"Conferência que nunca reprova não está conferindo nada."**

Antes de confiar em qualquer conferidor automatizado, teste se ele realmente rejeita entregas com defeito:
1. Crie uma cópia de teste com defeito deliberado (ex.: tela preta, teste quebrado, palavra proibida).
2. Execute a conferência e certifique-se de que ela acusa o erro com código 1 (`CONSERTAR`).
3. O argumento `--sonda` no `conferir_video.py` realiza essa validação automaticamente inserindo 1,5s de tela preta e silêncio em uma fatia temporária. Se o conferidor não acusar o erro, ele aborta acusando que a conferência está cega!

### 6. Subagente Revisor Cego (`revisor.md`)
Quem gerou o código tem viés de confirmação e tende a justificar as próprias falhas.  
Crie um subagente independente com permissões exclusivas de leitura (`Read, Glob, Grep`) que lê apenas o arquivo final e o `SPEC.md`:
```bash
/code-review
# ou invoque o revisor customizado:
"Use o subagente revisor para auditar o PR contra o SPEC.md"
```

### 7. Ciclo de Imunização Contínua
Todo erro que escapar para a revisão humana deve virar imediatamente uma checagem nova:
1. Explique por que a checagem falhou.
2. Adicione a verificação no script/hook.
3. Plante o erro para provar a reprovação.
4. Valide a aprovação na versão correta.
5. Atualize o `CLAUDE.md`.

---

## 🎬 Motor Conferidor de Vídeo (`conferir_video.py`)

Localizado em [`scripts/conferir_video.py`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/scripts/conferir_video.py):

| Checagem | Filtro / Mecanismo FFmpeg | Critério de Reprovação |
|---|---|---|
| **Formato e Proporção** | `ffprobe -show_entries stream=width,height` | Reprova formato diferente do pedido; avisa fora de 9:16 |
| **Começo da Fala** | `silencedetect=noise=-35dB:d=0.05` | Reprova se a fala demorar mais de 0,5 s para iniciar |
| **Pausas Internas** | `silencedetect=noise=-35dB:d=0.05` | Reprova pausas sem áudio acima da tolerância (ex.: 0,6 s) |
| **Fim do Vídeo** | `silencedetect=noise=-35dB:d=0.05` | Reprova sobra de silêncio > 1,2 s; avisa corte brusco < 0,08 s |
| **Tela Preta** | `blackdetect=d=0.1:pix_th=0.10` | Reprova qualquer tela preta > 0,05 s no miolo do vídeo |
| **Congelamentos** | `freezedetect=n=0.003:d=2` | Avisa imagem estática por 2 s ou mais |
| **Volume & Loudness** | `ebur128=peak=true` | Avisa fora de -16 a -12 LUFS ou True Peak > -1 dBFS |
| **Cortes (Antes/Depois)** | `select='gt(scene,0.35)',showinfo` | Gera `corte_NN.jpg` lado a lado (0,2 s antes / 0,2 s depois) |
| **Folhas de Contato** | `fps=1/2,scale=270:-2,tile=4x3` | Gera matriz de 12 quadros/folha para inspeção visual do LLM |
| **Roteiro vs Fala** | `difflib.SequenceMatcher` | Compara `roteiro.txt` com `ouvido.txt` (trocas, omissões, acréscimos) |
| **Sonda (Anti-Cegueira)** | Injeção de 1,5 s de tela preta e silêncio | Reprova a conferência inteira se a sonda não for capturada |

### Execução Direta:
```bash
python conferir_video.py render/final.mp4 \
  --roteiro roteiro.txt \
  --ouvido ouvido.txt \
  --formato 1080x1920 \
  --pausa 0.6 \
  --sonda
```

---

## 📁 Arquivos e Recursos da Skill

- **Script Conferidor**: [`scripts/conferir_video.py`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/scripts/conferir_video.py)
- **Stop Hook Bash**: [`scripts/conferir_video_hook.sh`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/scripts/conferir_video_hook.sh)
- **Stop Hook PowerShell**: [`scripts/conferir_video_hook.ps1`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/scripts/conferir_video_hook.ps1)
- **Script de Teste de Sonda**: [`scripts/testar_sonda.py`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/scripts/testar_sonda.py)
- **Template CLAUDE.md**: [`templates/CLAUDE.md`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/templates/CLAUDE.md)
- **Template settings.json**: [`templates/settings.json`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/templates/settings.json)
- **Template Revisor Cego**: [`templates/revisor.md`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/templates/revisor.md)
- **10 Prompts Prontos**: [`templates/prompts-loop.md`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/templates/prompts-loop.md)
- **PDF Original do Guia**: [`resources/guia_loop_verificacao.pdf`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/resources/guia_loop_verificacao.pdf)
- **Markdown Completo do Guia**: [`resources/guia_loop_verificacao.md`](file:///C:/Users/Administrator/.gemini/config/skills/loop-de-verificacao/resources/guia_loop_verificacao.md)

---

## 🛡️ As 7 Regras de Segurança Antes do Trabalho Sem Supervisão

1. **Existe uma checagem binária**: Retorna estritamente `passou` (código 0) ou `falhou` (código 1).
2. **A checagem já reprovou um erro plantado**: Foi testada contra um defeito deliberado antes de entrar em produção.
3. **Prova explícita no encerramento**: O agente apresenta o comando rodado, o log de saída e prints.
4. **Teto de voltas e de gastos**: Limites ativos via `--max-turns` (ex.: 30) ou `--max-budget-usd`.
5. **Revisor cego de fora**: Um subagente ou segunda sessão sem o histórico da conversa audita a entrega.
6. **Aprovação humana nos pontos sem volta**: Publicações no ar, disparos de mensagens, uploads de campanhas e deploys críticos exigem `Human-in-the-Loop`.
7. **Evolução contínua por imunização**: Todo erro identificado manualmente é convertido em nova checagem automatizada.
