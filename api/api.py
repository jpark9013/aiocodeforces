from api.apirequestmaker import CodeForcesRequestMaker

from api.return_objects.blog_entry import BlogEntry
from api.return_objects.comment import Comment
from api.return_objects.contest import Contest
from api.return_objects.hack import Hack
from api.return_objects.member import Member
from api.return_objects.party import Party
from api.return_objects.problem import Problem
from api.return_objects.problem_result import ProblemResult
from api.return_objects.problem_statistics import ProblemStatistics
from api.return_objects.ranklist_row import RanklistRow
from api.return_objects.rating_change import RatingChange
from api.return_objects.recent_action import RecentAction
from api.return_objects.submission import Submission
from api.return_objects.user import User


def _to_blog_entry(dic):
    return BlogEntry(dic["id"], dic["originalLocale"], dic["creationTimeSeconds"], dic["authorHandle"], dic["title"],
                     dic["content"], dic["locale"], dic["modificationTimeSeconds"], dic["allowViewHistory"],
                     dic["tags"], dic["rating"])


def _to_comment(dic):
    return Comment(dic["id"], dic["creationTimeSeconds"], dic["commentatorHandle"], dic["locale"], dic["text"],
                   dic["parentCommentId"], dic["rating"])


def _to_contest(dic):
    return Contest(dic["id"], dic["name"], dic["type"], dic["phase"], dic["frozen"], dic["durationSeconds"],
                   dic["startTimeSeconds"], dic["relativeTimeSeconds"], dic["preparedBy"], dic["websiteUrl"],
                   dic["description"], dic["difficulty"], dic["kind"], dic["icpcRegion"], dic["country"], dic["city"],
                   dic["season"])


def _to_hack(dic):
    return Hack(dic["id"], dic["creationTimeSeconds"], _to_party(dic["hacker"]), _to_party(dic["defender"]),
                dic["verdict"], _to_problem(dic["problem"]), dic["test"], dic["judgeProtocol"])


def _to_member(dic):
    return Member(dic["handle"])


def _to_party(dic):
    members = [_to_member(i) for i in dic["members"]]
    return Party(dic["contestId"], members, dic["participantType"], dic["teamId"], dic["teamName"], dic["ghost"],
                 dic["room"], dic["startTimeSeconds"])


def _to_problem(dic):
    return Problem(dic["contestId"], dic["problemsetName"], dic["index"], dic["name"], dic["type"], dic["points"],
                   dic["rating"], dic["tags"])


def _to_problem_result(dic):
    return ProblemResult(dic["points"], dic["penalty"], dic["rejectedAttemptCount"], dic["type"],
                         dic["bestSubmissionTimeSeconds"])


def _to_problem_statistics(dic):
    return ProblemStatistics(dic["contestId"], dic["index"], dic["solvedCount"])


def _to_ranklist_row(dic):
    problem_results = [_to_problem_result(i) for i in dic["problemResults"]]
    return RanklistRow(_to_party(dic["party"]), dic["rank"], dic["points"], dic["penalty"], dic["successfulHackCount"],
                       dic["unsuccessfulHackCount"], problem_results, dic["lastSubmissionTimeSeconds"])


def _to_rating_change(dic):
    return RatingChange(dic["contestId"], dic["contestName"], dic["handle"], dic["rank"],
                        dic["ratingUpdateTimeSeconds"], dic["oldRating"], dic["newRating"])


def _to_recent_action(dic):
    return RecentAction(dic["timeSeconds"], _to_blog_entry(dic["blogEntry"]), _to_comment(dic["comment"]))


def _to_submission(dic):
    return Submission(dic["id"], dic["contestId"], dic["creationTimeSeconds"], dic["relativeTimeSeconds"],
                      _to_problem(dic["problem"]), _to_party(dic["author"]), dic["programmingLanguage"], dic["verdict"],
                      dic["testset"], dic["passedTestCount"], dic["timeConsumedMillis"], dic["memoryConsumedBytes"],
                      dic["points"])


def _to_user(dic):
    return User(dic["handle"], dic["email"], dic["vkld"], dic["openId"], dic["firstName"], dic["lastName"],
                dic["country"], dic["city"], dic["organization"], dic["contribution"], dic["rank"], dic["rating"],
                dic["maxRank"], dic["maxRating"], dic["lastOnlineTimeSeconds"], dic["registrationTimeSeconds"],
                dic["friendOfCount"], dic["avatar"], dic["titlePhoto"])


class Client(CodeForcesRequestMaker):
    """The main Client for making requests through the CF API."""

    async def get_blog_entry_comments(self, ID):
        """Gets a list of comment objects. Takes in one argument, ID."""

        result = await self._get_result("blogEntry.comments", blogEntryId=ID)
        return [_to_comment(i) for i in result]