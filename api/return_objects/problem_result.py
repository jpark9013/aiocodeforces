"""The ProblemResult class for the CodeForces API."""

from dataclasses import dataclass


@dataclass
class ProblemResult:
    """https://codeforces.com/apiHelp/objects#ProblemResult"""

    points: float
    penalty: int
    rejected_attempt_count: int
    type: int  # Enum: PRELIMINARY, FINAL
    best_submission_time_seconds: int
