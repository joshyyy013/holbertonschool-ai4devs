# Reflection on AI-Assisted Debugging

## Introduction

In this exercise, I used an AI assistant to analyse five buggy snippets
written in Python, JavaScript, and Java. The bugs covered syntax, logic,
runtime exceptions, loop boundaries, and data types. I recorded the AI’s
diagnoses, applied corrections in separate files, tested their behaviour,
and documented the results. The exercise helped me examine both the
practical value of AI and my responsibility for checking its suggestions.

## AI Strengths

The easiest bugs for the AI were the missing Python colon and the
incorrect discount calculation. Both had clear causes and required small
changes. The AI also identified the JavaScript off-by-one error and
explained how accessing an index beyond the array returned undefined,
eventually producing NaN.

The Java integer-division explanation was particularly useful. The AI
explained that assigning a result to double does not prevent integer
division from happening first. Casting an operand before division
produced the expected 37.5%. These explanations connected the corrections
to language behaviour rather than simply supplying replacement code.
Overall, AI made diagnosis and documentation faster.

## AI Weaknesses

The Python average example required the most discussion because correctness
involved more than preventing an exception. An empty list should display
a no-scores message, while non-empty lists should preserve fractional
averages. My initial correction used floor division, which the AI
identified when I showed it the code.

The AI’s validation guidance also had a limitation. It initially documented
the fractional-average test as unconfirmed, and the checker rejected that
gap. This showed that a correct implementation and a passing example do
not establish complete validation. The AI should have helped select a
test that distinguished normal division from floor division earlier.

## Human Role

My trust in the suggestions was conditional. The changes looked reasonable,
but I needed to run them and compare actual outputs with expected results.
Recognising an explanation is different from proving that the corrected
code behaves properly.

Manual intervention was also necessary during setup. The Windows terminal
could not locate Python, so I switched to Anaconda Prompt. Java compilation
revealed a filename mismatch and an accidental variable typo. These issues
required attention to the actual environment and files, not just the
original bug descriptions.

Human judgement was needed to decide what an empty average should mean.
Returning zero avoids an exception, but displaying zero could incorrectly
suggest that a student received a genuine score of zero.

## Conclusion

AI was effective at explaining familiar errors and suggesting focused
corrections, but it did not replace testing or judgement. In real-world
debugging, I would provide relevant logs, expected behaviour, and
reproduction steps, then verify suggestions with representative and edge
cases. I also want to attempt diagnoses independently before consulting
AI. This would preserve my coding practice while allowing AI to support
the investigation rather than perform all the reasoning for me.