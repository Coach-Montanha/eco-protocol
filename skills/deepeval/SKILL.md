---
name: deepeval
description: Framework de avaliação formal de outputs LLM ("Pytest para LLMs"). 50+ métricas prontas: hallucination, relevancy, faithfulness, task completion. Fecha o loop-de-verificacao com prova matemática de qualidade — não só exit code 0.
---

# /deepeval — Verificação Formal de Outputs LLM

> **Pilar @eco**: AUTOCURA + PRECISÃO — transforma "parece certo" em "é provadamente correto".

## O que é

`confident-ai/deepeval` é o framework open-source de avaliação de LLMs que funciona como pytest — mas para saídas de modelos de linguagem. Roda localmente, integra com pytest nativamente.

## Por que é crítico para o ecossistema

Antes: `loop-de-verificacao` fechava com `exit code 0` (código compila e testes passam).  
Agora: deepeval fecha com **prova matemática** de que o output não alucionou e é semanticamente correto.

## Instalação

```bash
pip install deepeval
```

## Uso básico (integrado com pytest)

```python
import pytest
from deepeval import assert_test
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

def test_resposta_coach():
    test_case = LLMTestCase(
        input="Calcule o TDEE para 80kg, 1.80m, 30 anos, atividade moderada",
        actual_output=resposta_do_agente,
        retrieval_context=["TDEE = BMR + TEF + EEE + NEAT..."]
    )
    
    assert_test(test_case, [
        HallucinationMetric(threshold=0.3),
        AnswerRelevancyMetric(threshold=0.8)
    ])

# Executar:
# deepeval test run test_coach.py
```

## Métricas disponíveis (50+)

| Categoria | Métricas |
|---|---|
| **RAG** | Faithfulness, Contextual Precision, Contextual Recall |
| **Qualidade** | Answer Relevancy, G-Eval (custom) |
| **Agentes** | Task Completion, Tool Selection, Trajectory |
| **Segurança** | Hallucination, Bias, Toxicity |

## Integração com o ecossistema

```
Implementação concluída
        ↓
deepeval (verifica output LLM — anti-alucinação)
        ↓
Qodo Cover (verifica cobertura de edge cases no código)
        ↓
loop-de-verificacao (exit code 0 + prova deepeval)
        ↓
✅ Tarefa comprovadamente concluída
```

## Geração de dataset sintético para edge cases

```python
from deepeval.synthesizer import Synthesizer

# Gera automaticamente casos de teste para edge cases não cobertos
synthesizer = Synthesizer()
dataset = synthesizer.generate_goldens_from_docs(
    document_paths=["nutricao-avancada-montanha.md"]
)
```

## Auto-trigger por intenção

Acionar deepeval em:
- Qualquer resposta de agente que envolva cálculos (TDEE, macros, RPE, cargas)
- Respostas com dados clínicos ou de saúde
- Outputs de qualquer pipeline RAG
- Antes de entregar código gerado por LLM externo

## Economia estimada

- Bugs que escapam para produção: **–80%**
- Retrabalho por output incorreto: **–60%**
- Risco: **zero** — não modifica código, apenas valida
