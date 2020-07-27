"""The BlogEntry class for the CodeForces API"""

from api.apirequestmaker import strip_dict


class BlogEntry:
    """https://codeforces.com/apiHelp/objects#BlogEntry"""

    def __init__(self, dic):
        dic = strip_dict(dic)
        self.id: int = dic["id"]
        self.original_locale: str = dic["originalLocale"]
        self.creation_time_seconds: int = dic["creationTimeSeconds"]
        self.author_handle: str = dic["authorHandle"]
        self.title: str = dic["title"]
        self.locale: str = dic["locale"]
        self.modification_time_seconds: int = dic["modificationTimeSeconds"]
        self.allow_view_history: bool = dic["allowViewHistory"]
        self.tags: list = dic["tags"]  # Of strings
        self.rating: int = dic["rating"]
        self.content: str = dic.get("content")

    def __eq__(self, other):
        return isinstance(other, BlogEntry) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
