---
name judicial: impeccable
name: impeccable
description: Paul Bakaus Impeccable Design System Skill. Enforces strict aesthetic guardrails, visual hierarchy, typography scales, and component systems to eliminate generic AI UI patterns.
---

# Impeccable Design Guardrails Skill

Use this skill to audit or build frontend interfaces with strict design system guardrails.

## Core Aesthetic Guardrails

1. **Hierarchy & Contrast**:
   - Primary text: High contrast (`text-slate-100` / `#F8FAFC`).
   - Muted text: Subtle contrast (`text-slate-400` / `#94A3B8`). Never use washed-out low-contrast gray.
2. **Spacing Grid**: Enforce consistent 4-point spacing scale (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`).
3. **Component Guardrails**:
   - Buttons: Clear primary vs secondary visual weight with `:focus-visible` outline.
   - Cards: Subtle borders (`border-slate-800`), dark background cards (`bg-slate-900/90`), and refined inner padding (`p-4` to `p-6`).
4. **DESIGN.md Alignment**: Respect project-specific `DESIGN.md` tokens if present.
