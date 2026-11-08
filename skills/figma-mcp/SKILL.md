---
name: figma-mcp
description: Conexão de arquivos e design tokens do Figma diretamente ao contexto do agente para implementação fiel.
---

# Figma MCP — Design-to-Code Context Skill

Use this skill when reading Figma design files, extracting component tokens, and translating Figma designs into code.

## Key Capabilities

1. **Inspect Figma Node**: Read layout properties (auto-layout flex direction, padding, gap, alignment), background colors, border radius, and typography tokens from a Figma node ID.
2. **Design Tokens Extraction**: Map Figma variables (colors, spacing, font sizes) to Tailwind CSS classes or CSS variables.
3. **One-Shot Design to Code**: Convert Figma JSON node trees directly into clean React/Vue/HTML components.
4. **Tools**:
   - `figma_get_file`: Retrieve top-level document structure and frames.
   - `figma_get_node`: Extract detailed styling, layout, and child elements for a specific node.
