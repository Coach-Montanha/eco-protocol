---
name: replica
description: Framework clean-room para engenharia reversa e reconstrução independente de sistemas e UIs.
---

# 🧬 /replica — Hub Mestre de Engenharia Reversa & Reconstrução Clean-Room

O `/replica` consolida todas as modalidades de descompilação, análise visual, extração de arquitetura e recriação limpa de software (web, mobile, binários ou APKs) em um pipeline automatizado de 5 etapas:

---

## 1. Roteamento Inteligente de Entrada
O `/replica` detecta automaticamente o formato do alvo e aciona a estratégia adequada:
- **Alvo APK / Binário / Firmware (`engenhariareversadeep`, `apktool-modifier`, `rea`)**:
  - Descompilação local (Apktool, Ghidra), inspeção de `smali`, strings de conexão, tráfego de rede e permissões.
- **Alvo Visual / Telas / URLs (`engenhariareversavisual`, `clonar-interface-mimic`, `screenshot-to-code`)**:
  - Extração de layouts, tokens de design, componentes UI e conversão fiel em código Tailwind CSS + React via Microsoft Edge.
- **Sistema Completo (`engenhariareversafull`)**:
  - Engenharia reversa ponta a ponta em 5 fases com reconstrução limpa (clean-room).

---

## 2. O Ciclo Clean-Room em 5 Fases

```
 [ 1. RECON ] ➔ [ 2. MODELAGEM SQL/API ] ➔ [ 3. REBRAND & TOKENS ] ➔ [ 4. BUILD CIRÚRGICO ] ➔ [ 5. DIFF & GATE ]
```

1. **Fase 1 — Reconhecimento (`replica-recon`)**:
   - Inventário de telas, fluxos de autenticação, matriz de funcionalidades e endpoints.
2. **Fase 2 — Arquitetura & Banco (`replica-architect`, `replica-backend`)**:
   - Esquemas SQL relacionais para SQLite/PocketBase, regras de acesso e rotas REST/Hono sem tecnologias infladas.
3. **Fase 3 — Design System & Rebranding (`replica-design`, `replica-brand`)**:
   - Paleta de cores com contraste verificado (WCAG), escalas tipográficas e componentes nativos livres de marcas de terceiros.
4. **Fase 4 — Construção por Fatias Verticais (`replica-build`)**:
   - Código escrito do zero, 100% autoral, sem copiar código ou ativos proprietários do alvo.
5. **Fase 5 — Paridade & Testes (`replica-diff`, `replica-test`, `replica-launch`)**:
   - Comparação estrutural de telas, testes Playwright end-to-end e liberação pelo portão do gatekeeper.

---

## 3. Aliases Integrados
Os seguintes comandos satélites agora são roteados diretamente para o `/replica`:
- `/engenhariareversa`, `/engenhariareversadeep`, `/engenhariareversavisual`, `/engenhariareversafull`, `/clonar-interface-mimic`, `/screenshot-to-code`.
