---
name: graphify
description: >-
  Index codebases and generate zero-token AST knowledge graph reports (GRAPH_REPORT.md and graph.json).
  Use when the user requests /graphify, codebase analysis, architecture map, or token-efficient project inspection.
---

# Graphify — Knowledge Graph Generator & Zero-Token Context Indexer

Graphify statically analyzes project files, dependencies, routes, and components to construct an instant Knowledge Graph without consuming LLM context tokens.

## How to Run Graphify

To index the current workspace or target directory:

```bash
node C:\Users\Administrator\.gemini\config\sidecars\graphify.js [directory_path]
```

## Generated Outputs

1. `graphify-out/GRAPH_REPORT.md`: Primary architectural summary for AI agents (god nodes, imports, functions, entry points).
2. `graphify-out/graph.json`: Raw node/edge dependency graph.
3. `graphify-out/graph.html`: Interactive web visualization of the codebase graph.

## Agent Workflow Guidelines

- **First Action:** Read `graphify-out/GRAPH_REPORT.md` before reading raw source files when exploring a new or complex project.
- **Token Optimization:** Rely on the knowledge graph index to target exact line edits, reducing file read operations by up to 70x.
