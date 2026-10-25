---
name: omniroute
description: Dynamic LLM Routing and Token Economy Engine for Antigravity. Automatically classifies prompts and assigns optimal model tiers (flash_lite, flash, pro) to maximize token savings while ensuring 100% data privacy.
---

# OmniRoute — Dynamic LLM Token Economy Skill

Use OmniRoute to classify subagent tasks, optimize token consumption, and monitor token savings.

## Usage Guidelines

1. **Routing Strategy**:
   - `flash_lite`: For documentation lookups, quick code greps, file reads, and status checks. Saves ~85% tokens.
   - `flash`: For standard coding, feature implementation, and UI component edits. Saves ~65% tokens.
   - `pro`: For architectural redesigns, complex cross-file refactoring, and multi-agent coordination.

2. **Sidecar Integration**:
   - Execute sidecar classification: `node C:\Users\Administrator\.gemini\config\sidecars\omniroute.js`

3. **Data Security & Confidentiality**:
   - 100% local execution.
   - Zero remote logging or telemetry.
