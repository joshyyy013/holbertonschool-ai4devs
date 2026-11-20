# Risk Assessment — Express.js 3.21.2

## Project and assessment scope

- **Project:** Express.js, legacy release `3.21.2` (2015)
- **Source:** https://github.com/expressjs/express/tree/3.21.2
- **Assessment date:** 20 November 2026
- **Scope:** Source code and declared dependencies of Express 3.21.2, plus risks to applications continuing to use it. This is a **desk-based risk assessment**, not a runtime penetration test or a confirmed vulnerability scan.
- **Severity scale:** **High** = significant security, compatibility, or service impact; **Medium** = material maintainability or reliability impact; **Low** = limited impact or mainly operational inconvenience. Severity reflects likely impact and urgency, not a measured probability.

## Prioritized risk table

| ID | Risk | Severity | Evidence / notes | Recommended mitigation |
| --- | --- | --- | --- | --- |
| R1 | Unsupported end-of-life framework | **High** | Express officially marks the 3.x line as end-of-life; maintenance and security fixes stopped in 2015. This exposes applications to unresolved future defects. [1] | Plan a tested migration to a currently supported Express release; isolate or restrict exposure until migration. |
| R2 | Legacy dependency and supply-chain exposure | **High** | `package.json` pins old packages, including `connect@2.30.2`, `send@0.13.0`, and `cookie@0.1.3`. Old versions increase audit and upgrade difficulty. This table does **not** assert that every package/version has a confirmed vulnerability. [2] | Generate a software bill of materials; run a version-specific dependency audit; review advisories, update dependencies and retest. |
| R3 | Breaking changes during modernisation | **High** | Express 3-to-4 migration changes middleware integration, removes or deprecates old patterns, and changes APIs. Existing applications may break if upgraded without preparation. [3] | Create an endpoint inventory and regression baseline, then migrate incrementally with integration tests and rollback procedures. |
| R4 | Request parameter ambiguity | **Medium** | `req.param()` checks route parameters, request body, then query string using the same name; callers may not realise which input wins (`lib/request.js`, lines 290–298). The API was subsequently deprecated. [3][4] | Replace with explicit `req.params`, `req.body`, or `req.query` access and validate expected types and origins. |
| R5 | Complex router control flow and error handling | **Medium** | `Router.prototype._dispatch()` nests route matching, parameter callbacks, error callbacks and recursive continuation (`lib/router/index.js`, lines 83–174), making changes harder to reason about. [5] | Add characterization tests for route order, error propagation and parameter handling; split responsibilities if refactoring. |
| R6 | Broad response method with many branches | **Medium** | `res.send()` manages overloads, content types, body conversion, length, ETags, 304/204 handling, and HEAD semantics in one function (`lib/response.js`, lines 95–192). [6] | Add behavior-focused tests for status codes, headers, content negotiation and body handling before modifying it. |
| R7 | Legacy Node.js/runtime assumptions | **Medium** | The manifest declares `node >= 0.8.0` and uses historically old tooling. This is **not** a guarantee that the release works safely or correctly on modern supported Node.js versions. [2] | Test against a supported runtime in an isolated environment; document compatibility blockers and remove obsolete APIs during migration. |
| R8 | Reliance on historical test tooling | **Medium** | The repo includes tests, but its manifest uses older `mocha@2.2.5`, `supertest@1.0.1`, and `istanbul@0.3.9`. Existing tests may need updates to run reliably in today's toolchain. [2] | First run and record the original test suite in a controlled environment; modernize test dependencies and add CI for supported runtimes. |

## Priority order

1. **Immediate:** Address **R1** and **R2** before deploying or continuing to expose any production system using Express 3; verify exposure and audit the actual installed dependency tree.
2. **Before migration:** Reduce **R3** by mapping application routes, middleware and behaviors, creating regression tests, and arranging rollback.
3. **During refactoring:** Work through **R4–R8** with focused tests and incremental, reviewable changes.

## Important limitations

- The Express security history documents older vulnerabilities such as directory traversal and open redirects, **some of which were fixed within the Express 3.x series**. They should not automatically be claimed as still exploitable in `3.21.2`. [1]
- Findings **R4–R6** are source-level maintenance or misuse risks; they are **not proof of an active exploit**.
- No application-specific configuration, production deployment, installed lockfile, or live test results were provided. Actual likelihood and residual risk must be revisited after those are examined.

## Sources

1. Express.js, *Security updates* — https://expressjs.com/en/advanced/security-updates/
2. Express.js v3.21.2, `package.json` — https://github.com/expressjs/express/blob/3.21.2/package.json
3. Express.js, *Migrating from 3.x to 4.x* — https://github.com/expressjs/express/wiki/Migrating-from-3.x-to-4.x
4. Express.js v3.21.2, `lib/request.js` — https://github.com/expressjs/express/blob/3.21.2/lib/request.js
5. Express.js v3.21.2, `lib/router/index.js` — https://github.com/expressjs/express/blob/3.21.2/lib/router/index.js
6. Express.js v3.21.2, `lib/response.js` — https://github.com/expressjs/express/blob/3.21.2/lib/response.js
