---
name: taste-skill
description: Leon Lin Design Taste Skill for AI Agents. Infers design intent (editorial, brutalist, minimal, luxury), audits existing UI, and eliminates generic boilerplate landing pages.
---

# Taste Skill — Frontend Design Taste Framework

Use this skill to infer design vibes, audit existing landing pages, and guide high-taste visual decisions.

## Directives & Workflows

1. **Infer Design Vibe**:
   - *Minimalist/SaaS*: Clean borders, monospace accents, dark mode slate (`#0B0F19`), high typography contrast.
   - *Editorial*: Serif headings, generous whitespace, warm muted backgrounds, asymmetric grid layouts.
   - *Brutalist*: High-contrast stark borders (`border-2 border-black`), bold typography, sharp shadow offsets.
2. **Audit Before Redesign**:
   - Inspect existing brand assets, color palette, and layout before modifying code to preserve identity.
3. **Anti-Slop Check**:
   - Eliminate standard 3-card features with centered icons.
   - Replace generic rounded buttons with custom styled interactive triggers.
