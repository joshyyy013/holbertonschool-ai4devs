# Unit Test Generation Prompt Template

**Category**: Testing

**Role**: Software Test Engineer

**Task**: Write unit tests for the supplied function based on its expected behaviour. Include normal, boundary, and invalid inputs. Isolate external dependencies where appropriate and avoid assuming that the current implementation is correct.

**Input Placeholder**:
- Language: [LANGUAGE]
- Function and dependencies: [FUNCTION_AND_DEPENDENCIES]
- Expected behaviour: [EXPECTED_BEHAVIOUR]
- Testing framework and version: [TEST_FRAMEWORK]
- Existing tests, or none: [EXISTING_TESTS]

**Expected Output Format**:
1. Runnable test code in a fenced code block, including necessary imports and setup.
2. A brief description of what each test verifies.
3. The command to run the tests.
4. Any assumptions or unresolved specification questions.

Do not claim the tests passed unless they were actually run.

