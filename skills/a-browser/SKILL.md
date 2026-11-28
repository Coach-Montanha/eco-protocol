---
name: a-browser
description: Navegacao Web Autonoma, Scraping Furtivo Antibot, Playwright e Handover Humano no Microsoft Edge com motor @eco integrado.
---

# 🌐 `/a-browser` — Navegação Web Autônoma, Scraping Furtivo & Handover no Microsoft Edge

O **`/a-browser`** é o hub central de automação web, coleta de dados sem bloqueios e navegação inteligente no Microsoft Edge do Ecossistema Montanha.
Funde oficialmente **7 skills satélites**: `agent-browser`, `stealth-browser`, `scrapling`, `ScrapeGraphAI`, `firecrawl`, `agent-reach`, `browser-handover`, `playwright`, `defuddle`.

---

## ⚡ Motor `@eco` & Padrão Microsoft Edge Only
- **Microsoft Edge Obrigatório**: Toda automação, Playwright e inspeção roda estritamente no Microsoft Edge (`channel: 'msedge'`), aproveitando cookies e sessão ativa do usuário.
- **Ingestão Zero-Tokens**: Conteúdos de páginas são convertidos localmente para Markdown limpo via `defuddle` ou `firecrawl` antes de qualquer inferência, poupando tokens de visão.

---

## 🧬 Ferramentas & Estratégias Fundidas

### 1. Scraping Furtivo & Antibot Adaptativo (`scrapling`, `stealth-browser`)
- Contorna Cloudflare, DataDome e desafios antibot locais sem gastar tokens.
- Emula assinaturas TLS reais, fingerprints HTTP/2 de navegadores de mesa e usa seletores adaptativos que não quebram com mudanças de classes CSS.

### 2. Extração Estruturada por Grafos (`ScrapeGraphAI`)
- Pipelines orientados a grafos que extraem dados estruturados (JSON) de sites com DOM caótico sem necessidade de manutenção manual de scrapers.

### 3. Varredura Pública de Redes Sociais (`agent-reach`)
- Leitura e monitoramento em lote de Twitter/X, Reddit, YouTube e GitHub sem chaves de API pagas.

### 4. Rastreamento em Lote & Documentações (`firecrawl`)
- Rastreamento completo de sites com saída pronta para ingestão em bases de conhecimento.

### 5. Ponte de Handover Humano (`browser-handover`)
- Quando um site exige CAPTCHA visual, 2FA por SMS ou checkout de pagamento, o agente pausa, abre a janela visível no Edge para o usuário concluir e retoma o controle autonomamente após a aprovação.
