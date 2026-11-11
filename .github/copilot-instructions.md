# Project AI Coding Instructions

These instructions guide GitHub Copilot when the `ide_workflow_integration` folder is opened as a workspace/repository root. If the entire `holbertonschool-ai4devs` repository is opened instead, move or copy this file to the repository's root `.github/copilot-instructions.md` (after checking for existing instructions).

## General rules
- Explain proposed changes briefly before making broad edits.
- Prefer minimal, readable changes that preserve existing behaviour.
- Do not invent APIs, dependencies, project structure, or passing test results.
- Ask for or inspect surrounding source before modifying unfamiliar code.
- Never hardcode credentials or expose environment variables or user data.
- Suggest tests and manual verification steps for code changes.

## Language-specific rules
- **Python:** Follow PEP 8; format with Black where configured; add type hints to public functions; prefer small functions; suggest pytest coverage for logic and edge cases.
- **JavaScript:** Follow existing ESLint/project conventions; use `const` by default, `let` where reassignment is required; use semicolons consistently; handle async errors explicitly.
- **Java / Spring Boot:** Use descriptive class and method names; keep controllers thin and business logic in services; validate inputs; use JUnit tests where applicable.
- **SQL:** Prefer parameterized queries; avoid string-building SQL with user input; use explicit columns rather than `SELECT *` in application queries.

## Specialized workflow: code review
When asked to review code:
1. Identify correctness bugs and security risks first.
2. Check edge cases, error handling, and test coverage.
3. Note potential performance or maintainability issues only where relevant.
4. Report findings by severity with file references and specific suggested fixes.
5. Do not assert code has been run or tests passed unless verified.

## Specialized workflow: test generation
When asked to generate tests, include normal cases, boundary cases and failures. Follow the project's existing test framework and conventions. Explain what each test protects against.

## Specialized workflow: documentation
When asked to document a function or feature, write concise Markdown explaining purpose, inputs, outputs, an example, and limitations. Keep docs consistent with the actual code.
