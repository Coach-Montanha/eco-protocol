---
name: code-floorplan
description: Mapeamento visual de arquitetura de código, fluxo de dados e health check sem sobrecarga de contexto.
---

# Code Floorplan — Mapeamento Visual & Health Check de Arquitetura

O **Code Floorplan** gera uma representação cartográfica navegável de qualquer projeto de software, dividindo a base de código em setores lógicos (plantas baixas), indicando o fluxo de dados e identificando pontos de risco arquitetural.

---

## 1. As 4 Camadas do Floorplan

```
┌────────────────────────────────────────────────────────┐
│ 1. SETORES DO SISTEMA (Entrypoints, Rotas, UI)         │
├────────────────────────────────────────────────────────┤
│ 2. MOTORES DE NEGÓCIO (Serviços, Handlers, Controllers)│
├────────────────────────────────────────────────────────┤
│ 3. PERSISTÊNCIA & DADOS (PocketBase, SQLite, Schema)   │
├────────────────────────────────────────────────────────┤
│ 4. PONTES EXTERNAS (APIs, Webhooks WhatsApp, MCPs)     │
└────────────────────────────────────────────────────────┘
```

---

## 2. Health Check Arquitetural (Auditoria Rápida)

Ao gerar o Floorplan de um projeto, avalie obrigatoriamente:

1. **Acoplamento Circular**: Arquivos A e B que se importam mutuamente, gerando vazamento de escopo.
2. **Arquivos Monolíticos (God Files)**: Módulos com mais de 300 linhas ou com mais de 5 responsabilidades distintas.
3. **Fugas de Segredos (Regra RLAUR)**: Chaves de API ou URLs privadas em código estático.
4. **Tratamento de Exceções**: Blocos `try/except` vazios que silenciam falhas de infraestrutura.
5. **Dependências Fantasmas**: Bibliotecas declaradas no `package.json` ou `requirements.txt` que nunca são importadas no projeto.

---

## 3. Como Gerar o Mapa no Ecossistema

Para mapear qualquer diretório local em formato visual Markdown para o Obsidian:

```bash
# Varredura hierárquica rápida de módulos e linhas de código
python -c "
import os
for root, dirs, files in os.walk('.'):
    # ignorar pastas infladas
    if any(p in root for p in ['node_modules', '.git', '__pycache__', 'dist', 'build']):
        continue
    code_files = [f for f in files if f.endswith(('.ts', '.js', '.py', '.html', '.css', '.go'))]
    if code_files:
        print(f'Setor: {root} ({len(code_files)} arquivos)')
        for f in code_files:
            size_lines = sum(1 for _ in open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore'))
            print(f'  - {f} [{size_lines}L]')
"
```

---

## 4. Conexão com o Ecossistema

- Complementa o [`graphify`](file:///C:/Users/Administrator/.gemini/config/plugins/efficiency-toolkit/skills/graphify/SKILL.md) e as ferramentas do plugin `understand-anything`.
- Serve como base de diagnóstico pré-refatoração para o [`gsd-core`](file:///C:/Users/Administrator/.gemini/config/plugins/efficiency-toolkit/skills/gsd-core/SKILL.md) e [`karpathy-skills`](file:///C:/Users/Administrator/.gemini/config/skills/karpathy-skills/SKILL.md).
