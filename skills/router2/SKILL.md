---
name: router2
description: Orquestrador leve e despachante cego para Groq / OpenRouter (Llama 3 70B), blindando tokens locais do Antigravity.
---

# Router2 — Modo Despachante Groq / OpenRouter

Ative com `/router2` ou `@router2`.

## Diretrizes de Execução

1. **Fase 1 — Despacho Imediato:**
   - Remove o prefixo `/router2`.
   - Zero reasoning/chain-of-thought interno no Antigravity.
   - Monta payload limpo para a API do Groq (`llama-3.3-70b-versatile`) ou OpenRouter.

2. **Fase 2 — Execução Externa:**
   - Instrução de retorno:
     *"Retorne apenas o resultado final estruturado e aplicável, sem saudações ou explicações desnecessárias."*

3. **Fase 3 — Entrega Final:**
   - Entrega direta do resultado ao usuário sem retrabalho, reinterpretação ou resumo.
