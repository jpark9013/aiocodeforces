from aiocodeforces.enum import ProblemResultType


class ProblemResult:

    __slots__ = ["points", "penalty", "rejected_attempt_count", "type", "best_submission_time_seconds"]

    def __init__(self, dic):
        self.points: float = dic["points"]
        self.penalty: int = dic["penalty"]
        self.rejected_attempt_count: int = dic["rejectedAttemptCount"]
        self.type: ProblemResultType = ProblemResultType[dic["type"]]  # Enum: PRELIMINARY, FINAL
        self.best_submission_time_seconds: int = dic["bestSubmissionTimeSeconds"]
