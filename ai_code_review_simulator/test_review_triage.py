"""Tests for review finding triage and report generation."""

import unittest

from review_triage import Decision, Finding, ReviewReport, Severity, Source


class ReviewReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = ReviewReport("Add review triage")
        self.report.add(
            Finding(
                "f-low",
                "Consider renaming this variable",
                Severity.LOW,
                Source.AI,
                "src/example.py",
                8,
            )
        )
        self.report.add(
            Finding("f-high", "Handle missing input", Severity.HIGH, Source.HUMAN)
        )

    def test_prioritized_puts_high_severity_first(self) -> None:
        self.assertEqual(
            [item.finding_id for item in self.report.prioritized()],
            ["f-high", "f-low"],
        )

    def test_decision_requires_a_rationale(self) -> None:
        with self.assertRaises(ValueError):
            self.report.decide("f-low", Decision.REJECTED, "  ")

    def test_decision_is_recorded_and_open_filter_updates(self) -> None:
        updated = self.report.decide(
            "f-high", Decision.ACCEPTED, "Missing input causes a crash."
        )
        self.assertEqual(updated.decision, Decision.ACCEPTED)
        self.assertEqual(updated.rationale, "Missing input causes a crash.")
        self.assertEqual(
            [item.finding_id for item in self.report.prioritized(open_only=True)],
            ["f-low"],
        )

    def test_duplicate_ids_and_unknown_decisions_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.report.add(Finding("f-low", "Duplicate", Severity.LOW, Source.AI))
        with self.assertRaisesRegex(KeyError, "unknown"):
            self.report.decide("missing", Decision.DEFERRED, "Needs discussion")
        with self.assertRaisesRegex(ValueError, "must be"):
            self.report.decide("f-low", Decision.OPEN, "Still reviewing")

    def test_finding_validates_line_and_global_location(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive"):
            Finding("bad", "Bad line", Severity.LOW, Source.AI, "a.py", 0)
        self.assertEqual(self.report.findings[1].location, "Global")
        self.assertEqual(self.report.findings[0].location, "src/example.py:8")

    def test_markdown_escapes_table_cells_and_includes_reason(self) -> None:
        report = ReviewReport("Review | title")
        report.add(Finding("f1", "Check A | B", Severity.MEDIUM, Source.AI))
        report.decide("f1", Decision.DEFERRED, "Discuss in next sprint")
        output = report.to_markdown()
        self.assertIn("# Review Triage: Review | title", output)
        self.assertIn("Check A \\| B", output)
        self.assertIn("Discuss in next sprint", output)

    def test_empty_report_has_a_placeholder(self) -> None:
        self.assertIn("No findings recorded", ReviewReport("Empty").to_markdown())


if __name__ == "__main__":
    unittest.main()