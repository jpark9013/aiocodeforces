import asyncio
import hashlib
import json
import random
import time
from abc import ABC
from collections import OrderedDict
from html.parser import HTMLParser
from io import StringIO

import aiohttp

from aiocodeforces.blog_entry import BlogEntry
from aiocodeforces.comment import Comment
from aiocodeforces.contest import Contest
from aiocodeforces.hack import Hack
from aiocodeforces.problem import Problem
from aiocodeforces.problem_statistics import ProblemStatistics
from aiocodeforces.ranklist_row import RanklistRow
from aiocodeforces.rating_change import RatingChange
from aiocodeforces.recent_action import RecentAction
from aiocodeforces.submission import Submission
from aiocodeforces.user import User


class HTTPError(Exception):
    pass


# THX https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class _MLStripper(HTMLParser, ABC):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


class Client:
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
    session: Optional[:class:`aiohttp.ClientSession`]
        Include an aiohttp ClientSession. Defaults to creating a new one.
    """

    _c = 0
    _anonymous = False
    _own_loop = False

    def __init__(self, api_key=None, secret=None, rand=None, strip_html=True, session=None):

        self._strip_html = strip_html

        try:
            self.loop = asyncio.get_running_loop()
        except RuntimeError:
            self.loop = asyncio.get_event_loop()
            self.loop.run_forever()
            self._own_loop = True

        if session is not None and not isinstance(session, aiohttp.ClientSession):
            raise TypeError(f"Expected client session for kwarg session, received {session} instead.")

        self._session = aiohttp.ClientSession() if session is None else session

        if not rand:
            self._rand = random.randint(0, 899999) + 100000
            self._staticrand = True

        elif not isinstance(rand, int):
            raise TypeError(f"Non integer passed in as random number: {rand}")

        elif rand > 999999 or rand < 100000:
            raise ValueError(f"Non 6 digit integer passed as rand: {rand}")

        else:
            self._rand = int(rand)
            self._staticrand = False

        if not api_key or not secret:
            self._anonymous = True
        else:
            self._api_key = api_key
            self._secret = secret

    def _strip_tags(self, html):
        s = _MLStripper()
        s.feed(html)
        return s.get_data()

    def _strip_dict(self, dic):
        if self._strip_html:
            if isinstance(dic, dict):
                for k in dic.keys():
                    dic[k] = self._strip_dict(dic[k])
            elif isinstance(dic, list):
                for i, v in enumerate(dic):
                    dic[i] = self._strip_dict(v)
            elif isinstance(dic, str):
                dic = self._strip_tags(dic)

        return dic

    def _get_url(self, method, **fields):

        if self._anonymous:
            url = [f"https://codeforces.com/api/{method}?"]

            for i, v in fields.items():
                url.append(f"{i}=")

                if isinstance(v, list):
                    for j in v:
                        url.append(f"{j};")
                else:
                    url.append(str(v))

                url.append("&")

            # Cut off the extra & at the end
            return "".join(url[:-1])

        else:
            if not self._staticrand:
                self.get_new_rand()

            url = [f"https://codeforces.com/api/{method}?"]
            fields["apiKey"] = self._api_key
            fields["time"] = str(int(time.time()))

            # Sort the field after adding apiKey and time params
            fields = OrderedDict(sorted([(i, v) for i, v in fields.items()]))

            for i, v in fields.items():
                url.append(f"{i}=")

                if isinstance(v, list):
                    for j in v:
                        url.append(f"{j};")
                else:
                    url.append(str(v))

                url.append("&")

            url.append(f"apiSig={self._rand}")

            # Extend this to url after doing hashing
            apiSig = [f"{self._rand}/{method}?"]

            for i, v, in fields.items():
                apiSig.append(f"{i}=")

                if isinstance(v, list):
                    for j in v:
                        apiSig.append(f"{j};")
                else:
                    apiSig.append(str(v))

                apiSig.append("&")

            apiSig = apiSig[:-1]
            apiSig.append(f"#{self._secret}")
            hash = hashlib.sha512(("".join(apiSig).encode("utf-8"))).hexdigest()

            url = f"{''.join(url)}{hash}"
            return url

    def get_new_rand(self, rand=None):

        if not rand:
            self._rand = random.randint(0, 899999) + 100000
        elif not isinstance(rand, int):
            raise TypeError(f"Non integer passed as rand: {rand}")
        elif rand > 999999 or rand < 100000:
            raise ValueError(f"Non 6 digit integer passed as rand: {rand}")
        else:
            self._rand = int(rand)

    async def _get_result(self, method, **fields):

        url = self._get_url(method, **fields)

        async with self._session.get(url) as resp:
            if resp.status == 404:
                raise HTTPError(f"Request failed: no such method {method}.")

            elif resp.status == 429 or resp.status == 503:
                self._c += 1
                if self._c < 10:
                    await asyncio.sleep(1)
                    await self._get_result(url)
                else:
                    raise HTTPError(f"Tried to get response from URL 10 times, however response failed.")

            self._c = 0

            body = json.loads(await resp.text())

        self._check_status(body)

        return self._strip_dict(body["result"])

    def _check_status(self, resp):
        if resp["status"] == "FAILED":
            raise HTTPError(f"Request failed: {resp['comment']}")

    def stop(self):
        """Stops the asyncio loop."""

        self.loop.stop()
        self.loop.close()

    def _remove_none(self, dic):
        return {k: dic[k] for k in dic if dic[k]}

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

        kwargs = {
            "contestId": contestID,
            "from": startIndex,
            "count": count,
            "handles": handles,
            "room": room,
            "showUnofficial": showUnofficial
        }

        result = await self._get_result("contest.standings", self._remove_none(kwargs))

        result["contest"] = Contest(result["contest"])
        result["problems"] = [Problem(i) for i in result["problems"]]
        result["rows"] = [RanklistRow(i) for i in result["rows"]]

        return result

    async def get_contest_status(self, contestID, handle=None, startIndex=None, count=None):
        """Returns a list of submission objects. Takes in 4 arguments. contestID, an int, is the only required one. The
        rest, handle, startIndex, and count, are str, int, and int, respectively."""

        kwargs = {
            "contestId": contestID,
            "handle": handle,
            "startIndex": startIndex,
            "count": count
        }

        result = await self._get_result("contest.status", self._remove_none(kwargs))
        return [Submission(i) for i in result]

    async def get_problems(self, tags=None, problemsetName=None):
        """Returns a tuple of two lists from a problemset. The first list of Problems, and the second is the list of
        ProblemStatistics. Takes in two optional arguments, tags (a list of strings), and problemset
        name (also a string)."""

        kwargs = {
            "tag": tags,
            "problemsetName": problemsetName
        }

        result = await self._get_result("problemset.problems", self._remove_none(kwargs))
        result[0] = [Problem(i) for i in result[0]]
        result[1] = [ProblemStatistics(i) for i in result[1]]

        return result

    async def get_problemset_submissions(self, count, problemsetName=None):
        """Returns a list of Submission objects, in decreasing order of submission ID. Two arguments: count, which is
        a required argument that is an int, and problemsetName, which is an optional argument that is a str."""

        kwargs = {
            "count": count,
            "problemsetName": problemsetName
        }

        result = await self._get_result("problemset.recentStatus", self._remove_none(kwargs))
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
            raise HTTPError("Cannot get friends when sending anonymous requests.")

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

        kwargs = {
            "handle": handle,
            "startIndex": startIndex,
            "count": count
        }

        result = await self._get_result("user.status", self._remove_none(kwargs))
        return [Submission(i) for i in result]
