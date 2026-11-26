"""Track and render decisions made during AI and human code reviews."""

from dataclasses import dataclass, replace
from enum import Enum
from typing import Iterable


class Severity(str, Enum):
    """Impact level assigned to a review finding."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Source(str, Enum):
    """Origin of a review finding."""

    AI = "AI"
    HUMAN = "Human"


class Decision(str, Enum):
    """Reviewer disposition for a finding."""

    OPEN = "open"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    DEFERRED = "deferred"


_SEVERITY_ORDER = {
    Severity.CRITICAL: 0,
    Severity.HIGH: 1,
    Severity.MEDIUM: 2,
    Severity.LOW: 3,
}
_FINAL_DECISIONS = {Decision.ACCEPTED, Decision.REJECTED, Decision.DEFERRED}


@dataclass(frozen=True)
class Finding:
    """One inline or global suggestion from a review."""

    finding_id: str
    message: str
    severity: Severity
    source: Source
    file_path: str | None = None
    line: int | None = None
    decision: Decision = Decision.OPEN
    rationale: str | None = None

    def __post_init__(self) -> None:
        if not self.finding_id.strip() or not self.message.strip():
            raise ValueError("finding_id and message are required")
        if self.line is not None and self.line < 1:
            raise ValueError("line must be a positive integer")
        if self.line is not None and not self.file_path:
            raise ValueError("a line number requires a file path")
        if self.file_path is not None and not self.file_path.strip():
            raise ValueError("file_path cannot be blank")
        if self.decision in _FINAL_DECISIONS and not (self.rationale or "").strip():
            raise ValueError("a rationale is required for a final decision")

    @property
    def location(self) -> str:
        """Return a readable file location or identify a global comment."""
        if self.file_path is None:
            return "Global"
        if self.line is None:
            return self.file_path
        return f"{self.file_path}:{self.line}"


class ReviewReport:
    """Collect review findings and produce a prioritized Markdown report."""

    def __init__(self, title: str, findings: Iterable[Finding] = ()) -> None:
        if not title.strip():
            raise ValueError("title is required")
        self.title = title
        self._findings: dict[str, Finding] = {}
        for finding in findings:
            self.add(finding)

    @property
    def findings(self) -> tuple[Finding, ...]:
        """Return findings as an immutable snapshot."""
        return tuple(self._findings.values())

    def add(self, finding: Finding) -> None:
        """Add a finding, rejecting duplicate IDs to avoid overwriting feedback."""
        if finding.finding_id in self._findings:
            raise ValueError(f"duplicate finding ID: {finding.finding_id}")
        self._findings[finding.finding_id] = finding

    def decide(self, finding_id: str, decision: Decision, rationale: str) -> Finding:
        """Record a justified disposition and return the updated finding."""
        if decision not in _FINAL_DECISIONS:
            raise ValueError("decision must be accepted, rejected, or deferred")
        finding = self._findings.get(finding_id)
        if finding is None:
            raise KeyError(f"unknown finding ID: {finding_id}")
        updated = replace(finding, decision=decision, rationale=rationale.strip())
        self._findings[finding_id] = updated
        return updated

    def prioritized(self, *, open_only: bool = False) -> tuple[Finding, ...]:
        """Sort findings by severity, keeping insertion order for ties."""
        candidates = self.findings
        if open_only:
            candidates = tuple(
                item for item in candidates if item.decision is Decision.OPEN
            )
        return tuple(sorted(candidates, key=lambda item: _SEVERITY_ORDER[item.severity]))

    def to_markdown(self) -> str:
        """Render a concise decision log suitable for a pull request."""
        rows = [
            f"# Review Triage: {self.title}",
            "",
            "| Severity | Source | Location | Decision | Finding | Rationale |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for finding in self.prioritized():
            values = (
                finding.severity.value,
                finding.source.value,
                finding.location,
                finding.decision.value,
                finding.message,
                finding.rationale or "—",
            )
            cells = [value.replace("|", "\\|").replace("\n", " ") for value in values]
            rows.append("| " + " | ".join(cells) + " |")
        if len(rows) == 4:
            rows.append("| — | — | — | — | No findings recorded | — |")
        return "\n".join(rows) + "\n"