---
name: a-seguranca
description: Portao Mestre de Auditoria de Seguranca, Blindagem de Credenciais RLAUR, Analise OWASP Top 10 e Revisao sem Falsos Positivos com motor @eco integrado.
---

# 🛡️ `/a-seguranca` — Auditoria Geral, OWASP & Blindagem de Credenciais

O `/a-seguranca` (ou `@a-seguranca`) é o portão inegociável de segurança para código, dependências, APIs e esteiras de CI/CD.
- **Skills Fundidas:** `security-audit` + `seguranca-api-keys` + `skillspector` + `open-kritt` + `coderabbit` + `review` + `ghostaction-defense` + `osint-footprint`.

---

## ⚡ Motor `@eco` Integrado & Gatekeeper
1. **Regra RLAUR de Blindagem**: Bloqueio total contra envio ou commit de `.env`, segredos, chaves de API ou dados confidenciais de alunos/clientes.
2. **Auditoria Estática sem Falsos Positivos (`open-kritt`)**: Análise cirúrgica de vulnerabilidades reais (SQLi, XSS, SSRF, RCE).
3. **Defesa GhostAction**: Inspeção de workflows do GitHub Actions para impedir injeções maliciosas.

---

## 🚦 Portão de Commit
- `git add .` e `git commit` são autorizados apenas com validação limpa de segurança.
- Em caso de falha, o `/a-seguranca` barra a execução e devolve o apontamento cirúrgico da linha com vulnerabilidade.

---
## 🔗 Conexões & Skills Relacionadas
- [[Sistemas/gatekeeper|gatekeeper]]
- [[Sistemas/security-audit|security-audit]]
- [[Sistemas/seguranca-api-keys|seguranca-api-keys]]
- [[Seguranca/skillspector|skillspector]]
- [[Sistemas/open-kritt|open-kritt]]
- [[Produtividade/eco|eco]]
