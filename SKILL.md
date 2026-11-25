---
name: eco
description: Motor mestre de ultra-eficiência do Antigravity. Unifica roteamento de modelos, despacho Groq/Gemini e diretrizes locais.
---

# /eco — Motor Mestre de Ultra-Eficiência

O motor **@eco** é o padrão operacional do ambiente.

## Quando Usar
- Em 100% das tarefas como diretriz silenciosa e contínua.
- Sempre que houver necessidade de economizar tokens em operações pesadas, tarefas de código ou pesquisas externas.

## Canais de Operação

### 1. Canal Interno (Tarefas Locais)
- **Leitura / Inspeção**: `flash_lite` (economia de ~85% de tokens).
- **Código / Testes**: `flash` (economia de ~65% de tokens).
- **Arquitetura Crítica**: `pro`.

### 2. Canal Externo (URLs / Páginas / Textos Extensos)
- **Groq Llama 3.3 70B**: Inferência ultra-rápida sem gastar tokens locais.
- **Gemini 2.5 Flash**: Fallback automático para grandes contextos (1M+ tokens).

## Telemetria Obrigatória
Toda resposta deve apresentar no final:
```markdown
---
🛠️ **Skills Utilizadas**:
- `/<nome-da-skill>`: Resumo do que executou.

---
📊 **Telemetria de Tokens @eco**:
- **Gasto Real**: ~X tokens
- **Sem Automação**: ~Z tokens (fluxo convencional não otimizado)
- **Economia Total**: ~K tokens poupados (~W%)
```
