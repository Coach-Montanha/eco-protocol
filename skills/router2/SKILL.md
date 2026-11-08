---
name: router2
description: Alias unificado para o Canal Externo do protocolo /eco (Despacho cego Groq Llama 3.3 70B com fallback Gemini 2.5 Flash).
---

# Router2 — Canal Externo do Protocolo @eco

> **Status:** Este protocolo foi fundido ao motor mestre **`/eco`** (sempre ativo como regra global).

Quando acionado via `/router2` ou `@router2`, ativa diretamente o **Canal Externo do `/eco`**:
- Despacho cego para Groq (`llama-3.3-70b-versatile`) com fallback transparente para Gemini 2.5 Flash API.
- Zero consumo de tokens de raciocínio (CoT) locais no Antigravity.
- Respostas puras, estruturadas e cirúrgicas sob as diretrizes Ponytail (sem saudações ou preâmbulos).
