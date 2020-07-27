from api.apirequestmaker import CodeForcesRequestMaker

from api.return_objects.blog_entry import BlogEntry
from api.return_objects.comment import Comment
from api.return_objects.contest import Contest
from api.return_objects.hack import Hack
from api.return_objects.hack import JudgeProtocol
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
    try:
        content = dic["content"]
    except KeyError:
        content = None

    return BlogEntry(dic["id"], dic["originalLocale"], dic["creationTimeSeconds"], dic["authorHandle"], dic["title"],
                     dic["locale"], dic["modificationTimeSeconds"], dic["allowViewHistory"],
                     dic["tags"], dic["rating"], content)


def _to_comment(dic):
    try:
        parentCommentId = dic["parentCommentId"]
    except:
        parentCommentId = None

    return Comment(dic["id"], dic["creationTimeSeconds"], dic["commentatorHandle"], dic["locale"], dic["text"],
                   parentCommentId, dic["rating"])


def _to_contest(dic):
    try:
        startTimeSeconds = dic["startTimeSeconds"]
    except KeyError:
        startTimeSeconds = None
    try:
        relativeTimeSeconds = dic["relativeTimeSeconds"]
    except KeyError:
        relativeTimeSeconds = None
    try:
        preparedBy = dic["preparedBy"]
    except KeyError:
        preparedBy = None
    try:
        websiteUrl = dic["websiteUrl"]
    except KeyError:
        websiteUrl = None
    try:
        description = dic["description"]
    except KeyError:
        description = None
    try:
        difficulty = dic["difficulty"]
    except KeyError:
        difficulty = None
    try:
        kind = dic["kind"]
    except KeyError:
        kind = None
    try:
        icpcRegion = dic["icpcRegion"]
    except KeyError:
        icpcRegion = None
    try:
        country = dic["country"]
    except KeyError:
        country = None
    try:
        city = dic["city"]
    except KeyError:
        city = None
    try:
        season = dic["season"]
    except KeyError:
        season = None

    return Contest(dic["id"], dic["name"], dic["type"], dic["phase"], dic["frozen"], dic["durationSeconds"],
                   startTimeSeconds, relativeTimeSeconds, preparedBy, websiteUrl, description, difficulty, kind,
                   icpcRegion, country, city, season)


def _to_hack(dic):
    try:
        verdict = dic["verdict"]
    except KeyError:
        verdict = None
    try:
        test = dic["test"]
    except KeyError:
        test = None
    try:
        d = dic["judgeProtocol"]
        judgeProtocol = JudgeProtocol(d["manual"], d["protocol"], d["verdict"])
    except KeyError:
        judgeProtocol = None

    return Hack(dic["id"], dic["creationTimeSeconds"], _to_party(dic["hacker"]), _to_party(dic["defender"]),
                verdict, _to_problem(dic["problem"]), test, judgeProtocol)


def _to_member(dic):
    return Member(dic["handle"])


def _to_party(dic):
    try:
        contestId = dic["contestId"]
    except KeyError:
        contestId = None
    try:
        teamId = dic["teamId"]
    except KeyError:
        teamId = None
    try:
        teamName = dic["teamName"]
    except KeyError:
        teamName = None
    try:
        room = dic["room"]
    except KeyError:
        room = None
    try:
        startTimeSeconds = dic["startTimeSeconds"]
    except KeyError:
        startTimeSeconds = None

    members = [_to_member(i) for i in dic["members"]]
    return Party(contestId, members, dic["participantType"], teamId, teamName, dic["ghost"], room, startTimeSeconds)


def _to_problem(dic):
    try:
        contestId = dic["contestId"]
    except KeyError:
        contestId = None
    try:
        problemsetName = dic["problemsetName"]
    except KeyError:
        problemsetName = None
    try:
        points = dic["points"]
    except KeyError:
        points = None
    try:
        rating = dic["rating"]
    except KeyError:
        rating = None

    return Problem(contestId, problemsetName, dic["index"], dic["name"], dic["type"], points, rating, dic["tags"])


def _to_problem_result(dic):
    return ProblemResult(dic["points"], dic["penalty"], dic["rejectedAttemptCount"], dic["type"],
                         dic["bestSubmissionTimeSeconds"])


def _to_problem_statistics(dic):
    try:
        contestId = dic["contestId"]
    except KeyError:
        contestId = None
    return ProblemStatistics(contestId, dic["index"], dic["solvedCount"])


def _to_ranklist_row(dic):
    problem_results = [_to_problem_result(i) for i in dic["problemResults"]]
    return RanklistRow(_to_party(dic["party"]), dic["rank"], dic["points"], dic["penalty"], dic["successfulHackCount"],
                       dic["unsuccessfulHackCount"], problem_results, dic["lastSubmissionTimeSeconds"])


def _to_rating_change(dic):
    return RatingChange(dic["contestId"], dic["contestName"], dic["handle"], dic["rank"],
                        dic["ratingUpdateTimeSeconds"], dic["oldRating"], dic["newRating"])


def _to_recent_action(dic):
    try:
        blogEntry = _to_blog_entry(dic["blogEntry"])
    except KeyError:
        blogEntry = None
    try:
        comment = _to_comment(dic["comment"])
    except KeyError:
        comment = None
    return RecentAction(dic["timeSeconds"], blogEntry, comment)


def _to_submission(dic):
    try:
        contestId = dic["contestId"]
    except KeyError:
        contestId = None
    try:
        verdict = dic["verdict"]
    except KeyError:
        verdict = None
    try:
        points = dic["points"]
    except KeyError:
        points = None
    return Submission(dic["id"], contestId, dic["creationTimeSeconds"], dic["relativeTimeSeconds"],
                      _to_problem(dic["problem"]), _to_party(dic["author"]), dic["programmingLanguage"], verdict,
                      dic["testset"], dic["passedTestCount"], dic["timeConsumedMillis"], dic["memoryConsumedBytes"],
                      points)


def _to_user(dic):
    try:
        firstName = dic["firstName"]
    except KeyError:
        firstName = None
    try:
        lastName = dic["lastName"]
    except KeyError:
        lastName = None
    try:
        country = dic["country"]
    except KeyError:
        country = None
    try:
        city = dic["city"]
    except KeyError:
        city = None
    try:
        organization = dic["organization"]
    except KeyError:
        organization = None
    return User(dic["handle"], dic["email"], dic["vkld"], dic["openId"], firstName, lastName, country, city,
                organization, dic["contribution"], dic["rank"], dic["rating"], dic["maxRank"], dic["maxRating"],
                dic["lastOnlineTimeSeconds"], dic["registrationTimeSeconds"], dic["friendOfCount"], dic["avatar"],
                dic["titlePhoto"])


class Client(CodeForcesRequestMaker):
    """The main Client for making requests through the CF API."""

    async def get_blog_entry_comments(self, ID):
        """Gets a list of comment objects. Takes in one argument, ID, which is an int."""

        result = await self._get_result("blogEntry.comments", blogEntryId=ID)
        return [_to_comment(i) for i in result]

    async def view_blog_entry(self, ID):
        """Get a BlogEntry object. Takes in one argument, ID, which is an int."""

        result = await self._get_result("blogEntry.view", blogEntryId=ID)
        return _to_blog_entry(result)

    async def get_contest_hacks(self, contestID):
        """Get a list of Hack objects. Takes in one argument, contestID, which is an int."""

        result = await self._get_result("contest.hacks", contestId=contestID)
        return _to_hack(result)

    async def get_contest_list(self, gym=False):
        """Returns a list of all avaliable contests. Takes in one argument, gym, which is a boolean. Defaults to
        false."""

        result = await self._get_result("contest.list", gym=gym)
        return [_to_contest(i) for i in result]

    async def get_contest_rating_changes(self, contestID):
        """Returns a list of RatingChange objects. Takes in one argument, contestID, which is an int."""

        result = await self._get_result("contest.ratingChanges", contestId=contestID)
        return [_to_rating_change(i) for i in result]

    async def get_contest_standings(self, contestID, startIndex=None, count=None, handles=None, room=None,
                                    showUnofficial=None):
        """Returns a dictionary with contest, problems, and rows being the three keys. The values are a Contest object,
        a list of Problem objects, and a list of RanklistRow objects respectively. Takes in 6 arguments, 5 of them being
        optional. The only required argument, contestID, is an int. The rest, startIndex, count, handles, room, and
        showUnofficial, are int, int, list, str, and boolean, respectively."""

        kwargs = {}
        if startIndex:
            kwargs["from"] = startIndex
        if count:
            kwargs["count"] = count
        if handles:
            kwargs["handles"] = handles
        if room:
            kwargs["room"] = room
        if showUnofficial:
            kwargs["showUnofficial"] = showUnofficial

        result = await self._get_result("contest.standings", **kwargs)

        result["contest"] = _to_contest(result["contest"])
        result["problems"] = [_to_problem(i) for i in result["problems"]]
        result["rows"] = [_to_ranklist_row(i) for i in result["rows"]]

        return result

    async def get_contest_status(self, contestID, handle=None, startIndex=None, count=None):
        """Returns a list of submission objects. Takes in 4 arguments. contestID, an int, is the only required one. The
        rest, handle, startIndex, and count, are str, int, and int, respectively."""

        kwargs = {}
        if handle:
            kwargs["handle"] = handle
        if startIndex:
            kwargs["startIndex"] = startIndex
        if count:
            kwargs["count"] = count

        result = await self._get_result("contest.status", **kwargs)
        return [_to_submission(i) for i in result]

    async def get_problems(self, tags=None, problemsetName=None):
        """Returns a tuple of two lists from a problemset. The first list of Problems, and the second is the list of
        ProblemStatistics. Takes in two optional arguments, tags (a list of strings), and problemset
        name (also a string)."""

        kwargs = {}
        if tags:
            kwargs["tags"] = tags
        if problemsetName:
            kwargs["problemsetName"] = problemsetName

        result = await self._get_result("problemset.problems", **kwargs)
        result[0] = [_to_problem(i) for i in result[0]]
        result[1] = [_to_problem_statistics(i) for i in result[1]]

        return result

    async def get_problemset_submissions(self, count, problemsetName=None):
        """Returns a list of Submission objects, in decreasing order of submission ID. Two arguments: count, which is
        a required argument that is an int, and problemsetName, which is an optional argument that is a str."""

        kwargs = {}
        if count:
            kwargs["count"] = count
        if problemsetName:
            kwargs["problemsetName"] = problemsetName

        result = await self._get_result("problemset.recentStatus", **kwargs)
        return [_to_submission(i) for i in result]

    async def get_recent_actions(self, maxCount=10):
        """Returns a list of RecentAction objects. Defaults to 10, use argument maxCount to change."""

        result = await self._get_result("recentActions", maxCount=maxCount)
        return [_to_recent_action(i) for i in result]

    async def get_blog_entries(self, handle):
        """Returns a list of BlogEntry objects from a user. Takes in one required argument, handle, which is a
        string."""

        result = await self._get_result("user.blogEntries", handle=handle)
        return [_to_blog_entry(i) for i in result]

    async def get_friends(self, onlyOnline=False):
        """Returns a list of friends's handles from the authorized user. Takes in one argument, onlyOnline, which
        defaults to False."""

        if self._anonymous:
            raise Exception("Cannot get friends when sending anonymous requests.")

        result = await self._get_result("user.friends", onlyOnline=onlyOnline)
        return result

    async def get_info(self, handles):
        """Returns a list of User objects. Takes in a single required argument, handles, which is a list of user
        handles."""

        result = await self._get_result("user.friends", handles=handles)
        return [_to_user(i) for i in result]

    async def get_rated_users(self, activeOnly=True):
        """Returns a list of users who are rated (have participated in at least one contest). Takes in an argument,
        activeOnly, which when True will only return users that have participated in contests in the last month.
        Defaults to True. This function also takes an immensely long time to execute, so it is not recommended to use
        it."""

        result = await self._get_result("user.ratedList", activeOnly=activeOnly)
        return [_to_user(i) for i in result]

    async def get_rating(self, handle):
        """Returns a list of RatingChange objects for the user. Required argument is a user handle, which is str."""

        result = await self._get_result("user.rating", handle=handle)
        return [_to_rating_change(i) for i in result]

    async def get_submissions(self, handle, startIndex=None, count=None):
        """Returns a list of Submission objects from the user, sorted decreasing by ID. Required arguments: user handle,
        str. Optional arguments: startIndex, count."""

        kwargs = {}
        if startIndex:
            kwargs["startIndex"] = startIndex
        if count:
            kwargs["count"] = count

        result = await self._get_result("user.status", **kwargs)
        return [_to_submission(i) for i in result]
