import asyncio
import hashlib
import json
import random
import time
from collections import OrderedDict

import aiohttp


class CodeForcesRequestMaker:
    """A base wrapper class for the Request maker."""

    _c = 0
    _anonymous = False
    loop = asyncio.get_event_loop()

    async def _session(self):
        with aiohttp.ClientSession() as session:
            self._session = session

    def __init__(self, api_key=None, secret=None, rand=None):
        """Initialize api key, secret, and random number, which is default between 100,000 and 999,999 inclusive."""

        self.loop.run_until_complete(self._session())

        if not rand:
            self._randnum = random.randint(0, 899999) + 100000
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

        self.loop.run_until_complete(self._session())

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
            apiSig = [str(self._rand) + "/", str(method) + "?"]

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

            hash = hashlib.sha512(("".join(apiSig).encode("utf-8")))

            url = f"{''.join(url)}apiSig={self._rand}{hash.hexdigest()}"
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
                if resp.status_code == 404:
                    raise Exception(f"Request failed: no such method.")

                elif resp.status_code == 429 or resp.status_code == 503:
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
