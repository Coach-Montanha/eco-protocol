---
name: writing-plans
description: Criação de planos granulares de implementação passo a passo para desenvolvimento guiado por specs.
---

# Writing Plans — Spec-Driven Development Skill

Use this skill to convert architectural specifications into rigorous, actionable implementation plans.

## Plan Structure Rules

1. **Granular Tasks**: Break work into small, incremental tasks that take 2–5 minutes to execute.
2. **Explicit File Paths**: Every task MUST specify the exact target file URI (`file:///path/to/file`) and precise functions/components.
3. **Verification Steps**: Each task MUST include an automated build/test command or concrete manual check to verify success before moving forward.
4. **No Shortcuts**: Explicitly state assumptions, edge cases, and dependency order (prerequisites first).
