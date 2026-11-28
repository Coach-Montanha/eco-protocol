---
name: context7
description: Servidor MCP da Upstash que injeta documentação versionada e precisa de bibliotecas diretamente no contexto do agente. Elimina alucinações de API em stacks como PocketBase, Hono, Playwright, Tailwind. Version-aware.
---

# /context7 — Documentação Versionada Sem Alucinação

> **Pilar @eco**: PRECISÃO — elimina 100% do retrabalho por alucinação de API.

## O que é

`upstash/context7` é um servidor MCP que busca documentação atualizada e precisa de bibliotecas diretamente da fonte oficial, injetando a versão exata que você usa no contexto do agente.

## Problema que resolve

LLMs alucinam APIs de frameworks em evolução rápida. Sem context7:
```
Agente usa PocketBase.create() → API mudou para PocketBase.collection().create()
→ Bug → Debug → Correção → Mais tokens gastos
```

Com context7:
```
context7 pocketbase@0.23 → Injeta doc exata → Código correto na primeira vez
```

## Instalação

```bash
# Adicionar ao config MCP do Antigravity
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

## Stacks cobertas no ecossistema Montanha

| Stack | Skill parceira | Uso |
|---|---|---|
| PocketBase | `pocketbase` | Backend Anti-SaaS |
| Hono | `hono` | Microsserviços e webhooks |
| Playwright | `playwright` | Testes E2E e browser |
| Tailwind CSS | `impeccable`, `replica-build` | UI/UX |
| React / Next.js | `astryx`, `replica-build` | Frontend |
| SQLite | `pocketbase`, `a-infra` | Persistência local |

## Uso via tool call

```
// No prompt do agente:
"Use context7 to fetch PocketBase 0.23 auth docs before implementing"

// O MCP injeta automaticamente a documentação correta no contexto
```

## Auto-trigger por intenção

Sempre que detectar implementação com stack conhecida, acionar context7 **antes** de escrever qualquer código:

- Palavras-chave: `PocketBase`, `Hono`, `Playwright`, `Tailwind`, `Remix`, `Prisma`, `Drizzle`
- Ação: `context7 <library>@<version>` → injeção silenciosa no contexto

## Economia estimada

- Alucinações de API: **~0%** (eliminação total)
- Retrabalho por doc desatualizada: **~0%**
- Risco: **zero** — read-only, dados de fonte oficial
