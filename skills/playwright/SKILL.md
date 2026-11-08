---
name: playwright
description: Automação de testes ponta a ponta (E2E) e regressão visual com Playwright no Microsoft Edge.
---

# Playwright E2E Testing & Automation Skill

Use this skill to write, execute, and debug end-to-end tests, visual regression checks, and automated user flows.

## Best Practices

1. **Locators**: Prefer user-facing locators (`getByRole`, `getByText`, `getByTestId`) over implementation-dependent CSS paths.
2. **Auto-Waiting**: Leverage Playwright's built-in auto-waiting rather than hardcoded `waitForTimeout()`.
3. **Execution Commands**:
   - Run E2E tests: `npx playwright test`
   - Run headed/UI mode: `npx playwright test --ui`
   - Generate test report: `npx playwright show-report`
4. **Mobile & Viewports**: Configure multi-viewport testing (`Desktop Chrome`, `Mobile Chrome`, `iPhone 13`).
