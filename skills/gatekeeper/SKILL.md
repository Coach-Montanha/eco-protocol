---
name: gatekeeper
description: Hub unificado de segurança, auditoria de código e qualidade pré-deploy. Funde coderabbit, review, open-kritt, security-audit e seguranca-api-keys.
---

# 🛡️ /gatekeeper — Auditoria de Código, Segurança & Pré-Deploy

O `/gatekeeper` estabelece a barreira de controle de qualidade antes de qualquer commit, deploy ou publicação de código no Ecossistema Montanha:

## 1. Módulos Integrados
- **`security-audit` & `open-kritt`**: Auditoria estrita contra vulnerabilidades (OWASP Top 10, injeções SQL, sanitização de entrada, escape de comandos).
- **`seguranca-api-keys`**: Detecção e blindagem imediata contra chaves de API, credenciais ou segredos expostos em código ou logs.
- **`coderabbit` & `review`**: Open Code Review automatizado focado em TypeScript/Go/Python, conformidade multi-tenant e boas práticas da Vercel Guidelines.

## 2. Checklist Obrigatório
- [ ] Nenhuma credencial ou token privado gravado em arquivos de código.
- [ ] Endpoints e webhooks protegidos com assinatura/validação de autenticação.
- [ ] Zero vulnerabilidades críticas ou quebras em testes de regressão.
- [ ] Tipagem forte e código em conformidade com o padrão Ponytail/Karpathy.

## 3. Exemplos Práticos
- Auditoria pré-commit:
  > `/gatekeeper revise as modificações do webhook do WhatsApp e valide se há vazamento de chaves ou endpoints desprotegidos.`
- Homologação de PR/Diff:
  > `/gatekeeper analise o git diff da branch de pagamentos antes de liberar para produção.`
