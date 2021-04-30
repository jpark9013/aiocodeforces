import asyncio
import hashlib
import json
import random
import time
import typing
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

    _c = 0
    _anonymous = False

    def __init__(self,
                 api_key: str = None,
                 secret: str = None,
                 rand: int = None,
                 strip_html: bool = True,
                 session: aiohttp.ClientSession = None) -> None:
        """

        Parameters
        ----------
        api_key
        secret
        rand
        strip_html
        session
        """
        self._strip_html = strip_html

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

    async def close(self) -> None:

        await self._session.close()
        self._session = None

    def _remove_none(self, dic):
        return {k: dic[k] for k in dic if dic[k]}

    async def get_blog_entry_comments(self, blog_entry_id: int) -> typing.List[Comment]:
        result = await self._get_result("blogEntry.comments", blogEntryId=blog_entry_id)
        return [Comment(i) for i in result]

    async def view_blog_entry(self, blog_entry_id: int) -> BlogEntry:
        result = await self._get_result("blogEntry.view", blogEntryId=blog_entry_id)
        return BlogEntry(result)

    async def get_contest_hacks(self, contest_id: int) -> Hack:
        result = await self._get_result("contest.hacks", contestId=contest_id)
        return Hack(result)

    async def get_contest_list(self, gym: bool = False) -> typing.List[Contest]:
        result = await self._get_result("contest.list", gym=gym)
        return [Contest(i) for i in result]

    async def get_contest_rating_changes(self, contest_id: int) -> typing.List[RatingChange]:
        result = await self._get_result("contest.ratingChanges", contestId=contest_id)
        return [RatingChange(i) for i in result]

    async def get_contest_standings(self,
                                    contest_id: int,
                                    start_index: int = None,
                                    count: int = None,
                                    handles: typing.List[str] = None,
                                    room: str = None,
                                    show_unofficial: bool = None) -> \
            typing.Tuple[Contest, typing.List[Problem], typing.List[RanklistRow]]:

        kwargs = {
            "contestId": contest_id,
            "from": start_index,
            "count": count,
            "handles": handles,
            "room": room,
            "showUnofficial": show_unofficial
        }

        result = await self._get_result("contest.standings", **self._remove_none(kwargs))

        contest = Contest(result["contest"])
        problems = [Problem(i) for i in result["problems"]]
        rows = [RanklistRow(i) for i in result["rows"]]

        return contest, problems, rows

    async def get_contest_status(self,
                                 contest_id: int,
                                 handle: str = None,
                                 start_index: int = None,
                                 count: int = None) -> typing.List[Submission]:

        kwargs = {
            "contestId": contest_id,
            "handle": handle,
            "startIndex": start_index,
            "count": count
        }

        result = await self._get_result("contest.status", **self._remove_none(kwargs))
        return [Submission(i) for i in result]

    async def get_problems(self, tags: typing.List[str] = None, problemset_name: str = None) \
            -> typing.Tuple[typing.List[Problem], typing.List[ProblemStatistics]]:

        kwargs = {
            "tag": tags,
            "problemsetName": problemset_name
        }

        result = await self._get_result("problemset.problems", **self._remove_none(kwargs))
        problems = [Problem(i) for i in result[0]]
        problem_statistics = [ProblemStatistics(i) for i in result[1]]

        return problems, problem_statistics

    async def get_problemset_submissions(self, count: int, problemset_name: str = None) -> typing.List[Submission]:

        kwargs = {
            "count": count,
            "problemsetName": problemset_name
        }

        result = await self._get_result("problemset.recentStatus", **self._remove_none(kwargs))
        return [Submission(i) for i in result]

    async def get_recent_actions(self, max_count: int = 10) -> typing.List[RecentAction]:
        result = await self._get_result("recentActions", maxCount=max_count)
        return [RecentAction(i) for i in result]

    async def get_blog_entries(self, handle: str) -> typing.List[BlogEntry]:
        result = await self._get_result("user.blogEntries", handle=handle)
        return [BlogEntry(i) for i in result]

    async def get_friends(self, only_online: bool = False) -> typing.List[str]:
        if self._anonymous:
            raise HTTPError("Cannot get friends when sending anonymous requests.")

        result = await self._get_result("user.friends", onlyOnline=only_online)
        return result

    async def get_info(self, handles: typing.List[str]) -> typing.List[User]:
        result = await self._get_result("user.friends", handles=handles)
        return [User(i) for i in result]

    async def get_rated_users(self, active_only: bool = True) -> typing.List[User]:
        result = await self._get_result("user.ratedList", activeOnly=active_only)
        return [User(i) for i in result]

    async def get_rating(self, handle: str) -> typing.List[RatingChange]:
        result = await self._get_result("user.rating", handle=handle)
        return [RatingChange(i) for i in result]

    async def get_submissions(self, handle: str, start_index: int = None, count: int = None) -> typing.List[Submission]:

        kwargs = {
            "handle": handle,
            "startIndex": start_index,
            "count": count
        }

        result = await self._get_result("user.status", **self._remove_none(kwargs))
        return [Submission(i) for i in result]
