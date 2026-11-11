# AI Assistant Configuration

## Objective
Introduce a consistent AI-assisted workflow in Visual Studio Code, building on the workflow recorded in `workflow_baseline.md`. The goal is to reduce debugging and documentation overhead without sacrificing understanding or quality.

## IDE and assistant
- **Editor:** Visual Studio Code (VS Code).
- **Selected AI assistant:** GitHub Copilot (proposed for this task; local installation and account access are **not yet verified**).
- **Optional existing tool:** Chat-based AI assistance for explanations and second opinions. Do not claim this is integrated into VS Code.
- **Recommended VS Code extensions:** GitHub Copilot, Python, Pylance, and language-appropriate Java/JavaScript tooling. Confirm what is actually installed before reporting the setup as complete.

## Configuration files
1. **`.copilot-settings.yaml`** — assignment-readable manifest describing language-specific rules, code review, test generation and documentation workflows. **GitHub Copilot does not natively load this YAML file.** It is a Holberton submission artifact.
2. **`.github/copilot-instructions.md`** — natural-language instructions supported by GitHub Copilot in VS Code when placed at the **workspace/repository root**. This is the file that provides the effective assistant behaviour.

> Location note: These files are stored under `ide_workflow_integration/` for this assignment. If you normally open `holbertonschool-ai4devs/` as your VS Code workspace, place a copy of `copilot-instructions.md` at `holbertonschool-ai4devs/.github/copilot-instructions.md` (merge with any existing file). The nested file alone might not apply as repository-wide instructions when the whole repository is opened.

## Language-specific rules
| Language | AI guidance | Verification |
| --- | --- | --- |
| Python | PEP 8, Black formatting, type hints, small functions | Run project tests, preferably pytest where used |
| JavaScript | Respect ESLint/project rules, prefer `const`, consistent semicolons, explicit async errors | Run project linter/tests |
| Java (Spring Boot) | Thin controllers, service-layer logic, input validation | Run JUnit/Maven tests where applicable |
| SQL | Parameterized queries, explicit columns, safe handling of inputs | Inspect queries and test against a local database |

## Specialized AI workflows

### 1. Code review (primary)
1. Select a changed file or diff in VS Code.
2. Ask Copilot: **"Review this change for correctness, security, edge cases and maintainability. Rank issues by severity and suggest minimal fixes. Do not assume tests passed."**
3. Inspect the recommendations and apply only justified changes.
4. Run tests and compare the final diff before committing.

### 2. Test generation
1. Highlight a function or service.
2. Ask Copilot for tests covering happy paths, invalid inputs, boundaries and regressions using the existing test framework.
3. Review assertions, mocks, fixtures and assumptions.
4. Run the tests and repair issues manually as needed.

### 3. Documentation generation
1. Select a function or module.
2. Request concise Markdown documentation including purpose, inputs, outputs, example usage and constraints.
3. Confirm that the generated description matches the implementation.

## Local setup steps
1. Open VS Code and your `holbertonschool-ai4devs` repository.
2. Install/enable GitHub Copilot if available, and sign in to an eligible GitHub account.
3. Ensure `.github/copilot-instructions.md` exists at the **root of the opened repository**; copy/merge the supplied file there if necessary.
4. Keep `.copilot-settings.yaml` and this `ai_config.md` in `ide_workflow_integration/` for submission.
5. Ask Copilot to review a small Python or JavaScript snippet, then inspect its response and references to verify the instructions are being used.
6. Run tests before accepting AI-authored changes. Never upload tokens, passwords, `.env` values or private data to prompts.

## Measurement plan
Compare results against `workflow_baseline.md`: average time per development task, average bug-fix turnaround, commits per active week, and test outcomes. The current baseline estimates are not measured data, so record actual observations for a fair comparison.

## Setup verification status
- [x] Created assignment configuration manifest
- [x] Created Copilot instructions with language-specific guidance
- [x] Defined code review, test generation and documentation workflows
- [ ] Confirmed Copilot extension installed and signed in on local machine
- [ ] Confirmed instructions load in the user's VS Code workspace
- [ ] Tested a real code-review interaction and measured results

## References
- GitHub Docs: https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide
- VS Code Docs: https://code.visualstudio.com/docs/agent-customization/custom-instructions
