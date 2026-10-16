# Error Diagnosis Prompt Template

**Category**: Debugging

**Role**: Debugging Specialist

**Task**: Investigate the reported runtime or compilation error. Identify the likely cause using the evidence and propose the smallest suitable fix. State uncertainty if the evidence is incomplete.

**Input Placeholder**:
- Language and version: [LANGUAGE_VERSION]
- Relevant code: [CODE_BLOCK]
- Full error message: [ERROR_MESSAGE]
- Steps to reproduce: [REPRODUCTION_STEPS]

**Expected Output Format**:
1. The likely cause and supporting evidence.
2. Corrected code in a fenced code block.
3. Steps to verify the fix and expected results.

