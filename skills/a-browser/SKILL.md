---
name: a-browser
description: Navegacao Web Autonoma, Scraping Furtivo Antibot, Playwright e Handover Humano no Microsoft Edge com motor @eco integrado.
---

# 🌐 `/a-browser` — Automação Web, Scraping & Navegação Furtiva

O `/a-browser` (ou `@a-browser`) é o condutor unificado para toda navegação, extração de dados e automação web.
- **Skills Fundidas:** `agent-browser` + `stealth-browser` + `scrapling` + `playwright` + `browser-handover`.

---

## ⚡ Motor `@eco` Integrado & Microsoft Edge Standard
1. **Microsoft Edge Only**: Toda interação utiliza estritamente o Microsoft Edge (`msedge`) para aproveitar logins existentes e menor pegada de memória.
2. **Defuddle / Ingestão Zero-Tokens**: Converte páginas web diretamente em Markdown limpo antes de consumir tokens do modelo.
3. **Scrapling Adaptativo**: Contorna proteções Cloudflare e Turnstile localmente sem chamadas de visão computacional.

---

## 🔄 Protocolo de Handover Transparente
- O agente opera de forma autônoma até encontrar desafios interativos protegidos (CAPTCHA, 2FA, pagamento com cartão).
- Ao detectar essas barreiras, o `/a-browser` pausa a execução e devolve o controle instantaneamente à sua tela no Edge (`browser-handover`). Você resolve e o agente reassume o fluxo.

---
## 🔗 Conexões & Skills Relacionadas
- [[Automacao-Web-Scraping/agent-browser|agent-browser]]
- [[Automacao-Web-Scraping/browser-handover|browser-handover]]
- [[Automacao-Web-Scraping/playwright|playwright]]
- [[Desenvolvimento/scrapling|scrapling]]
- [[Sistemas/stealth-browser|stealth-browser]]
- [[Produtividade/eco|eco]]
