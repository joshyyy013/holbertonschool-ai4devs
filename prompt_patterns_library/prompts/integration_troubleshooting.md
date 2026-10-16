# Integration Troubleshooting Prompt Template

**Category**: Debugging

**Role**: Integration Engineer

**Task**: Investigate the failure between the supplied components. Rank likely causes using the available evidence and provide ordered diagnostic steps before proposing changes.

**Input Placeholder**:
- Components and versions: [COMPONENTS_AND_VERSIONS]
- Expected and actual behaviour: [EXPECTED_AND_ACTUAL_BEHAVIOUR]
- Relevant configuration with secrets removed: [CONFIGURATION]
- Request and response details with secrets removed: [REQUEST_RESPONSE_DETAILS]
- Logs with secrets removed: [LOGS]

**Expected Output Format**:
1. A ranked list of likely causes with supporting evidence.
2. Ordered diagnostic steps and what each result would indicate.
3. Proposed code or configuration changes.
4. A check of the complete workflow after the fix.

