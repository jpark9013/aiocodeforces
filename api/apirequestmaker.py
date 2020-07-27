import asyncio
import hashlib
import json
import random
import re
import time
from abc import ABC
from collections import OrderedDict
from io import StringIO
from html.parser import HTMLParser

import aiohttp


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


def _strip_tags(html):
    s = _MLStripper()
    s.feed(html)
    return s.get_data()


def strip_dict(dic):
    if striphtml:
        if isinstance(dic, dict):
            for k in dic.keys():
                dic[k] = strip_dict(dic[k])
        elif isinstance(dic, list):
            for i, v in enumerate(dic):
                dic[i] = strip_dict(v)
        elif isinstance(dic, str):
            dic = _strip_tags(dic)

    return dic


class CodeForcesRequestMaker:
    """A base wrapper class for the Request maker."""

    _c = 0
    _anonymous = False
    _own_loop = False

    def __init__(self, api_key=None, secret=None, rand=None, strip_html=True):
        """Initialize api key, secret, and random number, which is default between 100,000 and 999,999 inclusive."""

        try:
            self.loop = asyncio.get_running_loop()
        except RuntimeError:
            self.loop = asyncio.get_event_loop()
            self.loop.run_forever()
            self._own_loop = True

        self._session = aiohttp.ClientSession()

        if not rand:
            self._rand = random.randint(0, 899999) + 100000
            self._staticrand = True

        elif rand > 999999 or rand < 100000:
            raise Exception(f"Non 6 digit integer passed as rand: {rand}")

        else:
            self._rand = int(rand)
            self._staticrand = False

        if not api_key or not secret:
            self._anonymous = True
        else:
            self._api_key = api_key
            self._secret = secret

        global striphtml
        striphtml = strip_html

    def _get_url(self, method, **fields):
        """Get URL from method and fields. Example URL:
        https://codeforces.com/api/contest.hacks?contestId=566&apiKey=xxx&time=1595780434&apiSig=123456<hash>"""

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
        """Get a new 6-digit random integer."""

        if not rand:
            self._rand = random.randint(0, 899999) + 100000
        elif rand > 999999 or rand < 100000:
            raise Exception(f"Non 6 digit integer passed as rand: {rand}")
        else:
            self._rand = int(rand)

    async def _get_result(self, method, **fields):
        """Get result from method and fields."""

        url = self._get_url(method, **fields)

        try:
            async with self._session.get(url) as resp:
                if resp.status == 404:
                    raise Exception(f"Request failed: no such method.")

                elif resp.status == 429 or resp.status == 503:
                    self._c += 1
                    if self._c < 10:
                        await asyncio.sleep(1)
                        await self._get_result(url)
                    else:
                        raise Exception(f"Tried to get response from URL 10 times, however response failed.")

                self._c = 0

                body = json.loads(await resp.text())

        except json.decoder.JSONDecodeError as error:
            raise ValueError("Too many users.")

        self._check_status(body)

        return body["result"]

    def _check_status(self, resp):
        """Check the status of a response."""

        if resp["status"] == "FAILED":
            raise Exception(f"Request failed: {resp['comment']}")

    def stop(self):
        """Stops the loop if it was automatically created by the module."""

        if self._own_loop:
            self.loop.stop()
            self.loop.close()
