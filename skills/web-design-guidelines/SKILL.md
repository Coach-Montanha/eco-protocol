---
name: web-design-guidelines
description: Vercel-Labs Web Interface Guidelines & UI/UX Audit Skill. Audits HTML/CSS/React/Vue code against 100+ rules covering accessibility (ARIA, keyboard nav), performance, layout, and CWV standards.
---

# Web Design Guidelines Audit Skill

Use this skill to perform strict quality audits on web user interfaces and frontend code.

## Audit Checklists

1. **Accessibility (a11y)**:
   - Form inputs have explicit labels or `aria-label`.
   - Interactive elements have visible `:focus-visible` rings and keyboard accessibility (`tabIndex={0}`).
   - Contrast ratios pass WCAG AA standard (4.5:1 for normal text).

2. **Performance & Layout**:
   - Content-visibility and layout stability (zero Cumulative Layout Shift).
   - Touch targets on mobile are at least `44x44px`.
   - Prevent fixed overlay touch-traps by applying `display: none !important` when hidden.

3. **Output Format**:
   - Format audit findings in concise `file:line` format with clear severity badges (`[CRITICAL]`, `[HIGH]`, `[SUGGESTION]`).
