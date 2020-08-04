from api.apirequestmaker import CodeForcesRequestMaker

from api.return_objects.blog_entry import BlogEntry
from api.return_objects.comment import Comment
from api.return_objects.contest import Contest
from api.return_objects.hack import Hack
from api.return_objects.problem import Problem
from api.return_objects.problem_statistics import ProblemStatistics
from api.return_objects.ranklist_row import RanklistRow
from api.return_objects.rating_change import RatingChange
from api.return_objects.recent_action import RecentAction
from api.return_objects.submission import Submission
from api.return_objects.user import User


class Client(CodeForcesRequestMaker):
    """Represents a Client to make requests to the CodeForces API through.

    Parameters
    -----------
    api_key: Optional[:class:`int`]
        The API key to send requests to CodeForces API.
    secret: Optional[:class:`int`]
        The secret to send requests to CodeForces API.
    rand: Optional[:class:`int`]
        The random number to send requests to CodeForces API. Takes in a 6-digit integer, defaults to None.
    strip_html: Optional[:class:`bool`]
        Whether the library should parse out the HTML tags or not. Defaults to True.
    """

    async def get_blog_entry_comments(self, ID):
        """Gets a list of comment objects. Takes in one argument, ID, which is an int."""

        result = await self._get_result("blogEntry.comments", blogEntryId=ID)
        return [Comment(i) for i in result]

    async def view_blog_entry(self, ID):
        """Get a BlogEntry object. Takes in one argument, ID, which is an int."""

        result = await self._get_result("blogEntry.view", blogEntryId=ID)
        return BlogEntry(result)

    async def get_contest_hacks(self, contestID):
        """Get a list of Hack objects. Takes in one argument, contestID, which is an int."""

        result = await self._get_result("contest.hacks", contestId=contestID)
        return Hack(result)

    async def get_contest_list(self, gym=False):
        """Returns a list of all avaliable contests. Takes in one argument, gym, which is a boolean. Defaults to
        false."""

        result = await self._get_result("contest.list", gym=gym)
        return [Contest(i) for i in result]

    async def get_contest_rating_changes(self, contestID):
        """Returns a list of RatingChange objects. Takes in one argument, contestID, which is an int."""

        result = await self._get_result("contest.ratingChanges", contestId=contestID)
        return [RatingChange(i) for i in result]

    async def get_contest_standings(self, contestID, startIndex=None, count=None, handles=None, room=None,
                                    showUnofficial=None):
        """Returns a dictionary with contest, problems, and rows being the three keys. The values are a Contest object,
        a list of Problem objects, and a list of RanklistRow objects respectively. Takes in 6 arguments, 5 of them being
        optional. The only required argument, contestID, is an int. The rest, startIndex, count, handles, room, and
        showUnofficial, are int, int, list, str, and boolean, respectively."""

        kwargs = {"contestId": contestID}
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

        result["contest"] = Contest(result["contest"])
        result["problems"] = [Problem(i) for i in result["problems"]]
        result["rows"] = [RanklistRow(i) for i in result["rows"]]

        return result

    async def get_contest_status(self, contestID, handle=None, startIndex=None, count=None):
        """Returns a list of submission objects. Takes in 4 arguments. contestID, an int, is the only required one. The
        rest, handle, startIndex, and count, are str, int, and int, respectively."""

        kwargs = {"contestId": contestID}
        if handle:
            kwargs["handle"] = handle
        if startIndex:
            kwargs["startIndex"] = startIndex
        if count:
            kwargs["count"] = count

        result = await self._get_result("contest.status", **kwargs)
        return [Submission(i) for i in result]

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
        result[0] = [Problem(i) for i in result[0]]
        result[1] = [ProblemStatistics(i) for i in result[1]]

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
        return [Submission(i) for i in result]

    async def get_recent_actions(self, maxCount=10):
        """Returns a list of RecentAction objects. Defaults to 10, use argument maxCount to change."""

        result = await self._get_result("recentActions", maxCount=maxCount)
        return [RecentAction(i) for i in result]

    async def get_blog_entries(self, handle):
        """Returns a list of BlogEntry objects from a user. Takes in one required argument, handle, which is a
        string."""

        result = await self._get_result("user.blogEntries", handle=handle)
        return [BlogEntry(i) for i in result]

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
        return [User(i) for i in result]

    async def get_rated_users(self, activeOnly=True):
        """Returns a list of users who are rated (have participated in at least one contest). Takes in an argument,
        activeOnly, which when True will only return users that have participated in contests in the last month.
        Defaults to True. This function also takes an immensely long time to execute, so it is not recommended to use
        it."""

        result = await self._get_result("user.ratedList", activeOnly=activeOnly)
        return [User(i) for i in result]

    async def get_rating(self, handle):
        """Returns a list of RatingChange objects for the user. Required argument is a user handle, which is str."""

        result = await self._get_result("user.rating", handle=handle)
        return [RatingChange(i) for i in result]

    async def get_submissions(self, handle, startIndex=None, count=None):
        """Returns a list of Submission objects from the user, sorted decreasing by ID. Required arguments: user handle,
        str. Optional arguments: startIndex, count."""

        kwargs = {"handle": handle}
        if startIndex:
            kwargs["startIndex"] = startIndex
        if count:
            kwargs["count"] = count

        result = await self._get_result("user.status", **kwargs)
        return [Submission(i) for i in result]
