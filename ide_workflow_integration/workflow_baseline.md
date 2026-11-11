Workflow Baseline
Purpose
Document my current software development workflow before introducing or expanding AI-assisted IDE tools. This baseline will help me compare productivity, code quality, and development speed after making changes.
Current IDE Setup
- Primary IDE: Visual Studio Code (VS Code), using its integrated terminal for running applications, tests, and Git commands.
- Languages and frameworks: Python, Java (Spring Boot), JavaScript, SQL, HTML/Thymeleaf, and some C++.
- Development tools: Git and GitHub for version control; GitHub Actions for CI; Docker Compose for local services; MySQL for database work; WSL/Windows terminal environments.
- Project-specific tools: Python virtual environments and packages for Python projects; Maven for Spring Boot projects; AWS services (Lambda, API Gateway, DynamoDB, S3) for cloud development.
- AI assistance: Occasionally use chat-based AI assistance for debugging, explanations, planning, and drafting code, while checking and adapting outputs manually.
- Extensions: Exact currently installed VS Code extensions have not been verified. Record these using the Extensions view (Ctrl+Shift+X) before treating them as part of the measured baseline. Possible project-specific extensions include Java, Python, and formatting support, but these should not be claimed as installed without checking.
Current Development Workflow
1. Review the task requirements and break them into smaller steps.
2. Open the project in VS Code, inspect the existing code and relevant files, and create or switch to a Git branch when appropriate.
3. Implement features in small increments, using the integrated terminal to run the application.
4. Debug issues by reading errors and logs, searching code, and occasionally consulting AI assistance for possible explanations or fixes.
5. Run relevant tests locally and fix failures; for team projects, use GitHub Actions as an additional CI check.
6. Review changed files, commit descriptive changes, and push to GitHub.
Pain Points
1. Debugging unfamiliar code: Understanding errors across controllers, services, repositories, and databases can take considerable time.
2. Writing and maintaining tests: Creating test cases, setting up test data, and diagnosing failing tests can slow feature delivery.
3. Context switching: Moving between IDE, terminal, documentation, GitHub, and AI chat interrupts concentration.
4. Repetitive work: Boilerplate code, documentation updates, and routine checks take time away from implementing features.
5. Re-familiarising with languages: Switching between Java and Python can require reviewing syntax and library usage.
Productivity Metrics (Initial Estimates — Not Yet Measured)
Metric	Initial estimate	How to measure accurately
Average time per small development task	~90 minutes	Track start and finish times for five comparable tasks, then calculate the average.
Average bug-fix turnaround	~2 hours	Track time from starting investigation to a verified fix across five bugs.
Git commits per week	~5–10 during active development	Count commits authored in the selected repository over the last four active weeks.
Tests completed before a feature is merged	Not yet measured	Record number of tests written/run and pass rate per feature.

Baseline Analysis
The existing workflow supports full-stack development with testing and version control, but debugging, repetitive testing, and switching between tools may reduce productivity. The main improvement opportunities are faster understanding of unfamiliar code, assistance with first drafts of tests and documentation, and more consistent verification before commits.
Planned Comparison
After integrating AI tools into the IDE, repeat the same measurements on similarly sized tasks. Compare time per task, bug-fix turnaround, commits per week, and test results. Review AI-generated code manually to ensure that faster completion does not reduce quality.