---
name: a-seguranca
description: Portao Mestre de Auditoria de Seguranca, Blindagem de Credenciais RLAUR, Analise OWASP Top 10 e Revisao sem Falsos Positivos com motor @eco integrado.
---

# 🛡️ `/a-seguranca` (ou `/gatekeeper`, `@gatekeeper`) — Portão Mestre de Segurança & Auditoria

O **`/a-seguranca`** é a muralha de segurança obrigatória pré-commit e pré-deploy de todo o ecossistema, garantindo proteção contra vulnerabilidades, injeções e vazamentos de segredos.
Funde oficialmente **9 skills satélites**: `gatekeeper`, `Claude-BugHunter`, `security-audit`, `coderabbit`, `open-kritt`, `skillspector`, `ghostaction-defense`, `seguranca-api-keys`, `turnitout`, `osint-footprint`.

---

## ⚡ Motor `@eco` & Portão de Bloqueio RLAUR
- **Regra RLAUR Inegociável**: Bloqueio sumário e imediato se qualquer chave de API, segredo, senha ou dado confidencial de aluno for detectado em texto puro.
- **Portão Git Obrigatório**: Proibido executar `git add .`, `git commit` ou `git push` sem aprovação do gatekeeper.

---

## 🧬 Módulos de Auditoria Integrados

1. **Matrizes de Ataque & Bug Bounty (`Claude-BugHunter`)**:
   - Varredura orientada por relatórios reais do HackerOne e matrizes de ataque para identificar brechas em APIs, rotas e formulários.
2. **OWASP Top 10 sem Falsos Positivos (`open-kritt`, `security-audit`)**:
   - Verificação rigorosa de SQL Injection, Command Injection, Quebra de Autenticação (IDOR), SSRF e falhas de CORS.
3. **Defesa de CI/CD (`ghostaction-defense`)**:
   - Blindagem contra injeções de scripts maliciosos em workflows do GitHub Actions.
4. **Higienização Determinística (`turnitout`)**:
   - Remoção automática de caracteres invisíveis Unicode (*zero-width spaces*), rastreadores de IA e metadados C2PA antes do salvamento final.
