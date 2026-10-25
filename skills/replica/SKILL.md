---
name: replica
description: Esteira unificada de engenharia reversa e reconstrução de software. Funde o pacote replica-* (recon, architect, brand, design, build, backend, diff, test, launch), clonar-interface-mimic e screenshot-to-code.
---

# 🧬 /replica — Pipeline Unificado de Engenharia Reversa e Clonagem

O `/replica` consolida todas as etapas de desmontagem, análise e recriação limpa de aplicações web e mobile:

## 1. Módulos Integrados
- **Reconhecimento & Captura (`replica-recon`, `clonar-interface-mimic`, `screenshot-to-code`)**:
  - Extração de mapas de telas, fluxos de usuário e hierarquia visual a partir de URLs, APKs ou capturas de tela.
- **Arquitetura & Modelagem (`replica-architect`, `replica-backend`)**:
  - Definição de stack econômica (SQLite/PocketBase/Hono), modelagem relacional de banco e rotas de API.
- **Design & Tokens (`replica-design`, `replica-brand`)**:
  - Extração e recriação de tokens de cor, escala tipográfica, sombras e componentes Tailwind CSS sem usar marcas de terceiros.
- **Construção & Paridade (`replica-build`, `replica-diff`, `replica-test`, `replica-launch`)**:
  - Implementação em fatias verticais, diff estrutural de telas, testes automatizados e checklist de publicação.

## 2. O Ciclo em 4 Fases
```
 [ 1. RECON ] ➔ [ 2. DESIGN & SCHEMAS ] ➔ [ 3. BUILD CIRÚRGICO ] ➔ [ 4. DIFF & TEST ]
```

## 3. Exemplos Práticos
- Clonagem de tela:
  > `/replica recrie este layout do painel financeiro em Tailwind CSS + React puro com dados tipados para PocketBase.`
- Engenharia reversa completa:
  > `/replica analise o fluxo de agendamento do app X e gere a arquitetura completa em Hono + SQLite com testes de paridade.`
