---
name: coderabbit
description: CodeRabbit Automated Code Review & Security Skill. Audits diffs, detects bugs, verifies security vulnerabilities, and rates code quality before commit/push.
---

# CodeRabbit — Automated Code Review Skill

Use this skill to perform automated diff reviews and security scoring prior to git commit and push.

## Audit Checklist

1. **Bug & Logic Check**: Search for unhandled edge cases, null pointers, and broken async promises.
2. **Security & OWASP**: Check for exposed secrets, unescaped inputs, SQL/Command injections.
3. **Performance**: Verify bundle impact, memory leaks, and unnecessary re-renders.
4. **Scoring**: Assign a clear verdict (`APPROVED`, `CHANGES_REQUESTED`, `SECURITY_WARNING`).
