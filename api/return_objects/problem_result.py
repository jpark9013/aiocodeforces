"""The ProblemResult class for the CodeForces API."""

from api.apirequestmaker import strip_dict
from api.return_objects.enum import ProblemResultType


class ProblemResult:
    """
    Represents a Problem Result on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two ProblemResults are equal.

        ..describe: x != y

            Checks if two ProblemResults are not equal.

    Attributes
    -----------
    points: :class:``float``
        The amount of points for the ProblemResult.
    penalty: :class:``int``
        The penalty of the party for this problem.
    rejected_attempt_count: :class:``int``
        The number of rejected attempts for the problem.
    type: :class:``ProblemResultType``
        The ProblemResult type.
    best_submission_time_seconds: :class:``int``
        The best submission, in seconds after contest start, that brought maximum points to the Party.
    """

    __slots__ = ["points", "penalty", "rejected_attempt_count", "type", "best_submission_time_seconds"]

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.points: float = dic["points"]
        self.penalty: int = dic["penalty"]
        self.rejected_attempt_count: int = dic["rejectedAttemptCount"]
        self.type: ProblemResultType = ProblemResultType(dic["type"])  # Enum: PRELIMINARY, FINAL
        self.best_submission_time_seconds: int = dic["bestSubmissionTimeSeconds"]
