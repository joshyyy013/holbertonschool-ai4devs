# Performance Review Prompt Template

**Category**: Code Quality

**Role**: Performance Engineer

**Task**: Review the code for potential performance bottlenecks. Use the supplied workload and measurements to support your reasoning. Label unmeasured improvements as hypotheses and explain trade-offs.

**Input Placeholder**:
- Language: [LANGUAGE]
- Code: [CODE_BLOCK]
- Expected input sizes and workload: [WORKLOAD]
- Timing results, or none available: [TIMING_RESULTS]
- Constraints: [CONSTRAINTS]

**Expected Output Format**:
1. A table of potential bottlenecks, evidence, proposed improvements, and trade-offs.
2. Revised code snippets where useful.
3. A benchmark plan for comparing the original and revised code.

