"""The ProblemResult class for the CodeForces API."""

from api.apirequestmaker import strip_dict


class ProblemResult:
    """https://codeforces.com/apiHelp/objects#ProblemResult"""

    __slots__ = ["points", "penalty", "rejected_attempt_count", "type", "best_submission_time_seconds"]

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.points: float = dic["points"]
        self.penalty: int = dic["penalty"]
        self.rejected_attempt_count: int = dic["rejectedAttemptCount"]
        self.type: int = dic["type"]  # Enum: PRELIMINARY, FINAL
        self.best_submission_time_seconds: int = dic["bestSubmissionTimeSeconds"]
