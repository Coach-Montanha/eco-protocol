---
name: sequential-thinking
description: Servidor MCP oficial que força raciocínio estruturado step-by-step antes de qualquer ação. Elimina 30–50% de backtracking em tarefas arquiteturais. Zero config adicional — MCP oficial do protocolo.
---

# /sequential-thinking — Raciocínio Estruturado Pré-Ação

> **Pilar @eco**: PRECISÃO + ECONOMIA — estrutura o raciocínio antes de agir, reduzindo erros de rota e retrabalho.

## O que é

`modelcontextprotocol/sequential-thinking` é o servidor MCP oficial que força o agente a usar reflexão estruturada step-by-step antes de executar qualquer tarefa complexa.

## Como funciona

Ao invés de o agente "pular para o código", ele primeiro:

1. Decompõe o problema em pensamentos sequenciais encadeados
2. Avalia cada pensamento como hipótese
3. Revisa ou ramifica quando necessário
4. Só então executa a implementação

```json
// Exemplo de saída do MCP tool
{
  "thought": "O problema de NEAT=0 pode causar divisão por zero...",
  "nextThought": "Preciso validar antes de calc_tdee usar NEAT como divisor",
  "isRevision": false,
  "branchFromThought": null
}
```

## Instalação como MCP server

```bash
# Adicionar ao config MCP do Antigravity
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

## Quando acionar (auto-trigger por intenção)

- Refatorações multi-arquivo (3+ arquivos afetados)
- Debugging de bugs não triviais
- Design de nova arquitetura ou API
- Qualquer tarefa onde o blast radius é desconhecido

## Stack canônico com @eco

```
Tarefa complexa chegou
        ↓
sequential-thinking (mapeamento de hipóteses)
        ↓
ContextZero (blast radius — quais arquivos afetados)
        ↓
code-floorplan (validação estrutural)
        ↓
Implementação cirúrgica
        ↓
loop-de-verificacao (prova de conclusão)
```

## Economia estimada

- Redução de backtracking: **30–50%**
- Redução de tokens por erro de rota: **~35%**
- Risco: **zero** — adiciona estrutura, não substitui nenhuma skill
