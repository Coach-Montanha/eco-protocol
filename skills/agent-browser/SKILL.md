---
name: agent-browser
description: Navegação e automação web otimizada para IA via árvore de acessibilidade no Microsoft Edge.
---

# Agent Browser — Autonomous Navigation Skill

Use this skill for fast, reliable web browser automation, page scraping, form filling, and UI verification.

## Core Directives

1. **Accessibility Tree References**: Use stable accessibility tree ref IDs (`@e1`, `@e2`, `@e3`) instead of brittle CSS selectors.
2. **Fast Daemon Architecture**: Keeps browser session warm for multi-turn navigation.
3. **Structured JSON Output**: Returns crisp snapshot data (page title, text, active interactive targets) minimizing token usage.
4. **Commands**:
   - `open <url>`: Navigate to URL and print ref tree.
   - `click <ref>`: Click target element.
   - `type <ref> <text>`: Type into input field.
   - `screenshot`: Capture visual snapshot.
