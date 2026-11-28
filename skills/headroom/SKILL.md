---
name: headroom
description: Camada local de compressão de contexto para agentes de IA. Reduz tool outputs em 60–95% (JSON), 20% em código, via proxy transparente ou MCP server. Reversível e lossless via CCR. Aprende com falhas e corrige AGENTS.md automaticamente.
---

# /headroom — Motor de Compressão de Contexto Local

> **Pilar @eco**: ECONOMIA — maior ROI individual do arsenal. Zero degradação de qualidade.

## O que é

`headroomlabs-ai/headroom` é uma camada local de compressão de contexto que intercepta tráfego entre o agente e o modelo, comprimindo payloads antes que sejam faturados em tokens.

## Engines internas

| Engine | Alvo | Compressão |
|---|---|---|
| **SmartCrusher** | JSON payloads, nested objects, arrays | 60–95% |
| **CodeCompressor** | Código via Tree-sitter (AST-aware) | 30–60% |
| **Kompress-base** | Prosa, logs, traces | 20–40% |
| **CacheAligner** | Prefixos de prompt | Maximiza KV cache hits |
| **CCR** | Qualquer conteúdo | Lossless (reversível por hash) |

## Modos de integração

```bash
# 1. Instalar
pip install "headroom-ai[all]"

# 2a. Proxy transparente (zero mudança de código)
headroom proxy --port 8787

# 2b. MCP server nativo
headroom mcp install

# 2c. Wrapper direto do agente
headroom wrap claude
```

## Recurso crítico: `headroom learn`

```bash
headroom learn
```

Minera sessões de agente que falharam e escreve correções automáticas diretamente no `AGENTS.md` / `CLAUDE.md` do projeto — o agente aprende com seus próprios erros sem intervenção manual.

## MCP tools expostas

- `headroom_compress`: Comprime contexto arbitrário on-the-fly
- `headroom_retrieve`: Recupera conteúdo original via CCR (quando o modelo pede mais detalhes)
- `headroom_stats`: Exibe telemetria de economia acumulada

## Integração com @eco

Plugar como camada intermediária **antes** do Canal Externo (Groq/Gemini Flash):

```
Input → context-compress (skills) → headroom proxy → Groq/Gemini
                                   ↑
                            60–95% menos tokens nos outputs
```

## Economia estimada

- Tool outputs JSON: **60–95%**
- Código: **~20%**
- Workflow geral: **20–60%** de redução total de tokens
