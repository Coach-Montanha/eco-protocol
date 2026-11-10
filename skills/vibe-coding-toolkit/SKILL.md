---
name: vibe-coding-toolkit
description: Arquitetura de memory bank e orquestração de subagentes para tarefas longas de código.
aliases:
  - memory-bank-agentes
  - vibe-coding-matheus-gomes
---

# vibe-coding-toolkit

**Use quando:** Rodar tarefas complexas e demoradas com agentes de IA (que duram horas) e precisar evitar o esquecimento de contexto (*context drift*) e economizar até 90% da cota de tokens.

## 1. O que faz
1. **Padrão Memory Bank:** Divide a memória do projeto em arquivos estruturados (`productContext.md`, `activeContext.md`, `progress.md`) lidos sob demanda.
2. **Orquestração de Sub-agentes:** Permite que o agente principal delegue tarefas especializadas (leitura, escrita, testes) para sub-agentes paralelos sem sobrecarregar o histórico principal.
3. **Portões de Qualidade (Quality Gates):** Força testes automatizados antes de dar qualquer funcionalidade como concluída.

## 2. Repositório Local
- Caminho: `c:\Users\Administrator\Documents\Projetos\Pasta de Programas e Apps\vibe-coding-toolkit`

## 3. Como Disparar no seu Projeto
No chat do Antigravity:
> *"Aplique o setup do vibe-coding-toolkit neste projeto para estruturar o Memory Bank e rodar as tarefas em sub-agentes com economia de tokens."*

## 4. Conexões no Cofre
- [[gsd-core]] — Framework de fases (Discuss, Plan, Execute, Verify) baseado em contexto enxuto.
- [[roo-code]] — Modos Architect, Code, Debug com escopos bem delimitados.
- [[omniroute]] — Seleção dinâmica de modelo econômico por tarefa.
