# Edge Case Identification Prompt Template

**Category**: Testing

**Role**: Quality Assurance Analyst

**Task**: Identify meaningful edge cases that the existing tests do not cover. Derive expected results from the supplied rules, and mark results that need clarification.

**Input Placeholder**:
- Feature description: [FEATURE_DESCRIPTION]
- Validation and business rules: [VALIDATION_RULES]
- Existing tests, or none: [EXISTING_TEST_CASES]

**Expected Output Format**:
Return a table with these columns:
- Case ID.
- Input or condition.
- Expected result.
- Reason for testing.
- Priority.

Finish with any questions needed to resolve unclear expected results.

