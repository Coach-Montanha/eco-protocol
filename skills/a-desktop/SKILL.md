---
name: a-desktop
description: Automacao Nativa de Desktop do Windows via Acessibilidade, Controle de Emuladores Android e Terminal Remoto com motor @eco integrado.
---

# 🖥️ `/a-desktop` — Automação Nativa de Desktop do Windows, Emuladores & Terminal Remoto

O **`/a-desktop`** é o hub de controle e automação do sistema operacional Windows, aplicativos de desktop, emuladores Android e gerenciamento remoto por dispositivos móveis.
Funde oficialmente **11 skills satélites**: `agent-desktop`, `cli-anything`, `orca-agent`, `t3code`, `android-cli`, `android-device-hub`, `android-optimizer`, `simlock`, `resgatar-atalhos`, `openscreen`, `filee`, `compose-preview`.

---

## ⚡ Motor `@eco` & Computer Use via UI Automation
- **Automação sem Visão Computacional Pesada**: Em vez de tirar screenshots contínuos e gastar milhões de tokens de visão, o `/a-desktop` interage diretamente com a árvore de acessibilidade nativa do Windows (UI Automation) e APIs nativas em Rust (`agent-desktop`), operando formulários, botões e janelas com latência quase zero.

---

## 🧬 Módulos Integrados

1. **Wrappers CLI Automáticos (`cli-anything`)**:
   - Converte qualquer programa de desktop ou utilitário GUI em comandos de terminal estruturados, permitindo que os agentes operem ferramentas legadas diretamente pela linha de comando.
2. **Controle Remoto Seguro pelo Celular (`orca-agent`, `t3code`)**:
   - Relay seguro de terminal e mensagens para despachar ações, acompanhar builds e aprovar tarefas críticas pelo smartphone sem precisar estar na frente do computador.
3. **Otimização & Depuração Android via ADB (`android-optimizer`, `android-device-hub`)**:
   - Controle de emuladores e aparelhos físicos, debloat de processos inúteis, aceleração de GPU e compilação AOT para dispositivos com pouca memória (HY320, TV Boxes, tablets).
4. **Resgate & Organização de Atalhos do Windows (`resgatar-atalhos`)**:
   - Varredura e restauração de atalhos quebrados `.lnk` na Área de Trabalho e Menu Iniciar.
