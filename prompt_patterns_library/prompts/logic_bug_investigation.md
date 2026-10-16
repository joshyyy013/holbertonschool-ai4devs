# Logic Bug Investigation Prompt Template

**Category**: Debugging

**Role**: Software Debugger

**Task**: Compare expected and actual results to locate the faulty logic. Trace one failing example, then correct the code while preserving the intended behaviour.

**Input Placeholder**:
- Language: [LANGUAGE]
- Code: [CODE_BLOCK]
- Sample inputs: [SAMPLE_INPUTS]
- Actual outputs: [ACTUAL_OUTPUTS]
- Expected outputs: [EXPECTED_OUTPUTS]

**Expected Output Format**:
1. A brief trace showing where the result becomes incorrect.
2. Corrected code in a fenced code block.
3. A table of verification inputs and expected outputs.

