"""The RanklistRow class for the CodeForces API."""

from api.return_objects.party import Party
from api.return_objects.problem_result import ProblemResult


class RanklistRow:
    """https://codeforces.com/apiHelp/objects#RanklistRow"""

    def __init__(self, dic):
        self.party: Party = Party(dic["party"])
        self.rank: int = dic["rank"]
        self.points: float = dic["points"]
        self.penalty: int = dic["penalty"]
        self.successful_hack_count: int = dic["successfulHackCount"]
        self.unsuccessful_hack_count: int = dic["unsuccessfulHackCount"]
        self.problem_results: list = [ProblemResult(i) for i in dic["problemResults"]]  # of ProblemResult objects
        self.last_submission_time_seconds: int = dic.get("lastSubmissionTimeSeconds")  # Can be none.
