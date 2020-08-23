"""The RanklistRow class for the CodeForces API."""

from aiocodeforces.party import Party
from aiocodeforces.problem_result import ProblemResult


class RanklistRow:
    """
    Represents a ranklist row on CodeForces.

    ..container:: operations

        ..describe:: x == y

            Checks if two RanklistRows are equal.

        ..describe: x != y

            Checks if two RanklistRows are not equal.

    Attributes
    -----------
    party: :class:``Party``
        The party of the RanklistRow.
    rank: :class:``int``
        The rank of the party.
    points: :class:``float``
        The total number of points scored by the party.
    penalty: :class:``int``
        The total number of points penalized towards the party.
    successful_hack_count: :class:``int``
        The number of successful hack counts by the party.
    unsuccessful_hack_count: :class:``int``
        The number of unsuccessful hack counts by the party.
    problem_results: :class:``list``
        A list of ProblemResult objects, with party results for each object.
    last_submission_time_seconds: :class:``int``
        Time from contest start to last submission that scored points for the party.
    """

    __slots__ = ["party", "rank", "points", "penalty", "successful_hack_count", "unsuccessful_hack_count",
                 "problem_results", "last_submission_time_seconds"]

    def __init__(self, dic):
        self.party: Party = Party(dic["party"])
        self.rank: int = dic["rank"]
        self.points: float = dic["points"]
        self.penalty: int = dic["penalty"]
        self.successful_hack_count: int = dic["successfulHackCount"]
        self.unsuccessful_hack_count: int = dic["unsuccessfulHackCount"]
        self.problem_results: list = [ProblemResult(i) for i in dic["problemResults"]]  # of ProblemResult objects
        self.last_submission_time_seconds: int = dic.get("lastSubmissionTimeSeconds")  # Can be none.
