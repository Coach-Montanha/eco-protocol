---
name: sugestao-ativa
description: Protocolo comportamental de sugestão ativa e proativa. Define o formato padrão de toda resposta de código com sinalizações automáticas de risco, otimização disponível e próximo passo lógico — sem o usuário precisar perguntar.
---

# /sugestao-ativa — Protocolo de Sugestão Proativa

> **Pilar @eco**: SUGESTÃO ATIVA — antecipa o problema antes de você pedir.

## Conceito

A máquina perfeita de resolução de problemas não espera ser perguntada. Ela sinaliza proativamente:
- O risco que você não viu
- A otimização que vale 1 linha
- O próximo passo lógico

## Formato Padrão Obrigatório para Respostas de Código

```markdown
## ✅ Implementado
[código cirúrgico]

## ⚠️ Risco não solicitado
- [edge case que pode quebrar em produção]
- [dependência oculta ou comportamento não óbvio]

## 💡 Otimização disponível
[1 linha de código ou config — sem ensaio]

## 🔗 Próximo passo lógico
[sugestão direta do que vem depois — com comando ou código]
```

## Exemplo real

```python
# ✅ Implementado
def calc_tdee(bmr: float, tef: float, eee: float, neat: float) -> float:
    return bmr + tef + eee + neat
```

```
## ⚠️ Risco não solicitado
- NEAT pode ser 0.0 em sedentários — não usar como divisor sem validação
- Sem type guard: valores negativos em eee são aceitos silenciosamente

## 💡 Otimização disponível
@functools.lru_cache(maxsize=128) — se chamar mais de 1x por sessão com mesmos params

## 🔗 Próximo passo lógico
calc_macro_targets(tdee, goal="cut", protein_per_kg=2.2) ?
```

## Regras de Ativação

1. **Antes de implementar** (multi-arquivo): `sequential-thinking` mapeia impacto. Lista blast radius antes de escrever.
2. **Durante a implementação**: sinaliza edge cases não pedidos em linha (`# ⚠️`).
3. **Após implementar**: sempre apresenta risco, otimização e próximo passo.
4. **Em qualquer bug**: hipótese → teste → correção pontual. Stop-the-Line obrigatório.
5. **Em qualquer análise**: apresenta o "Objetivo Profundo" — o problema real por trás do descrito.

## Regras do que NÃO fazer

- ❌ Não escrever ensaios sobre a otimização — máximo 1 linha
- ❌ Não listar mais de 3 riscos (cap cognitivo ADHD)
- ❌ Não sugerir próximo passo óbvio demais ("testar o código")
- ❌ Não repetir o que já foi pedido explicitamente

## Integração com o ecossistema

Este protocolo é uma extensão comportamental de:
- `meta-prompt-deep`: eleva o pedido superficial ao objetivo profundo
- `karpathy-skills`: simplicidade radical, sem enrolação
- `loop-de-verificacao`: fecha com prova, não com achismo
- `debugging-and-error-recovery`: Stop-the-Line antes do chute

## Auto-trigger

**Sempre ativo.** Não requer invocação manual. Aplica-se a 100% das respostas de código.
