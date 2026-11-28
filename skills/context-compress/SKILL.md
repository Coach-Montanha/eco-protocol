---
name: context-compress
description: Compressão semântica seletiva de arquivos de instrução de agentes (SKILL.md, AGENTS.md, steering files). Aplica 0% em código e até 70% em prosa/paths, sem quebrar YAML frontmatter nem regras de comportamento.
---

# /context-compress — Compressor Semântico de Skills e Instruções

> **Pilar @eco**: ECONOMIA — especializado em reduzir o overhead das próprias skills em contexto ativo.

## O que é

`vidanov/context-compress` é um compressor que reconhece estrutura semântica de arquivos de instrução de agentes e aplica taxas de compressão diferenciadas por tipo de conteúdo.

## Taxas de compressão por tipo

| Tipo de conteúdo | Taxa aplicada | Motivo |
|---|---|---|
| Exemplos de código | **0%** | Preservação estrutural obrigatória |
| Regras e instruções críticas | **0–10%** | Comportamento do agente depende delas |
| Prosa explicativa | **40–60%** | Redundância natural da linguagem |
| Paths e referências | **50–70%** | Alta compressibilidade semântica |
| Listas de dependências | **40–60%** | Padrões repetitivos |

## Por que é diferente do LLMLingua

- LLMLingua comprime uniformemente → pode quebrar regras de comportamento
- `context-compress` lê YAML frontmatter + blocos de código + prosa → comprime **seletivamente**
- Zero risco de corromper instruções críticas de agente

## Uso típico

```bash
# Comprimir um SKILL.md antes de injetar em contexto
context-compress compress skills/healing/SKILL.md --output skills/healing/SKILL.min.md

# Comprimir o AGENTS.md global
context-compress compress rules/AGENTS.md --output rules/AGENTS.min.md --preserve-code
```

## Pipeline de integração com @eco

```
SKILL.md (bruto) → context-compress → SKILL.min.md (40–70% menor)
                                     ↓
                              Injeção em contexto ativo
```

## Casos de uso prioritários no ecossistema

1. **AGENTS.md global** (`rules/AGENTS.md`) — maior arquivo de instrução do ecossistema
2. **Skills volumosas**: `a-gsd`, `healing`, `loop-de-verificacao`, `a-coach-montanha`
3. **Pipeline pré-processamento**: antes de qualquer skill chaining de múltiplas skills

## Economia estimada

- AGENTS.md / SKILL.md complexos: **40–70% menos tokens em contexto ativo**
- Risco: **zero** — código e regras críticas ficam intactos por design
