---
name: emil-design-eng
description: Emil Kowalski UI & Motion Design Engineering Skill. Anti-slop craftsmanship guidelines for purposeful animations, natural easing curves, spring physics, and polished React micro-interactions.
---

# Emil Kowalski Design Engineering Skill

Use this skill when designing components, animations, and micro-interactions to prevent "AI slop" and ensure high visual craftsmanship.

## Motion & UI Directives

1. **Purposeful Motion**: Every animation must serve a function (e.g. feedback, spatial context, state transition). Avoid decorative wobble.
2. **Easing & Physics**:
   - Entrance: Fast in, smooth deceleration (`cubic-bezier(0.16, 1, 0.3, 1)`).
   - Exit: Quick acceleration out (`cubic-bezier(0.7, 0, 0.84, 0)`).
   - Spring: Dampened spring physics (`stiffness: 400`, `damping: 30`).
3. **Micro-Interactions**: Hover scales (1.02x max), active presses (0.97x), subtle backdrop blurs (`backdrop-blur-md`), and high-contrast borders (`border-slate-800/80`).
4. **Zero Slop**: Never use generic purple gradients or template cards. Use precise spacing (`4px` grid), crisp typography, and deliberate color tokens.
