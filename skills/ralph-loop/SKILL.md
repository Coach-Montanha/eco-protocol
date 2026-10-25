---
name: ralph-loop
description: Ralph Loop Autonomous Iteration Skill (Geoffrey Huntley Ralph Wiggum Technique). Runs persistent fresh-context turns using git & filesystem state until test suite passes 100%.
---

# Ralph Loop — Persistent Autonomous Iteration Skill

Use this skill for long-running autonomous execution loops without context rot.

## Ralph Loop Directives

1. **Filesystem as Source of Truth**: Use git history and file state rather than long chat transcripts.
2. **Fresh Context Iteration**: Each turn resets chat context while keeping code changes saved.
3. **Completion Criteria**: Loop terminates ONLY when all automated tests pass (`exit 0`) and zero lint errors remain.
4. **Safety Net**: Never run infinite loops; set max iteration threshold (default: 10 turns).
