"""The RanklistRow class for the CodeForces API."""

from dataclasses import dataclass

from api.return_objects.party import Party


@dataclass
class RanklistRow:
    """https://codeforces.com/apiHelp/objects#RanklistRow"""

    party: Party
    rank: int
    points: float
    penalty: int
    successful_hack_count: int
    unsuccessful_hack_count: int
    problem_results: list  # of ProblemResult objects
    last_submission_time_seconds: int  # Can be none.
