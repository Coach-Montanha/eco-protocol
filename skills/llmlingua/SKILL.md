---
name: llmlingua
description: Compressão de prompts e contextos volumosos via perplexidade (Microsoft). Até 20x compressão com mínima perda. LLMLingua-2 usa token-classification (3x–6x mais rápido). Ideal para skills de fisiologia, procedimentos e atas antes de injeção em contexto.
---

# /llmlingua — Compressão de Prompts por Perplexidade

> **Pilar @eco**: ECONOMIA — compressão de 40–80% em contextos com documentação pesada.

## O que é

`microsoft/LLMLingua` é uma família de ferramentas de compressão de prompt que usa modelos pequenos para calcular a importância de cada token e podar redundâncias, mantendo semântica.

## Família de ferramentas

| Versão | Abordagem | Velocidade | Melhor para |
|---|---|---|---|
| **LLMLingua** | Perplexidade + budget controller | Base | RAG, long-context |
| **LongLLMLingua** | Anti "lost-in-the-middle" | Base | Documentos longos |
| **LLMLingua-2** | Token-classification (ACL '24) | 3x–6x mais rápido | Produção, alta vazão |
| **SecurityLingua** | Compressão + defesa jailbreak | Base | Segurança integrada |

## Instalação e uso básico

```bash
pip install llmlingua

# Python — compressão de um contexto volumoso
from llmlingua import PromptCompressor

compressor = PromptCompressor(model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank")

compressed = compressor.compress_prompt(
    context,          # texto a comprimir
    rate=0.6,         # taxa conservadora para skills técnicas
    force_tokens=["TDEE", "RPE", "PocketBase"]  # preservar termos críticos
)
```

## Taxa conservadora por tipo de conteúdo

| Conteúdo | `rate` recomendado |
|---|---|
| Skills de fisiologia / nutrição | `0.6` (conservador) |
| Procedimentos e atas | `0.5` |
| Documentação de API | `0.7` (agressivo — context7 substitui melhor) |
| Fórmulas matemáticas (TDEE, RPE) | Usar `force_tokens` obrigatoriamente |

## Pipeline de integração com @eco

```
anydoc (PDF/DOCX → MD) → LLMLingua-2 (40–80% menor) → contexto limpo
                                                        ↓
                                          Skills: a-coach-montanha, nutricao,
                                          extrair-procedimento, a-procedimento
```

## Integração com LangChain / LlamaIndex

```python
from langchain.retrievers import ContextualCompressionRetriever
# Suporte nativo — zero código adicional
```

## Economia estimada

- Skills volumosas de fisiologia/nutrição: **40–80%**
- Documentos e atas: **50–70%**
- Redução de latência (LLMLingua-2): **3x–6x** vs v1
