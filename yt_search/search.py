from . import errors
import requests
import json
from . import obj


class build():
    def __init__(self, APIKey=None):
        if not APIKey:
            raise errors.MissingAPIKey()
        self.key = APIKey

    def search(self, Keyword, Max=5, Type=["video", "channel", "playlist"]):
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {"type": ','.join(Type), "maxResults": Max, "part": "snippet",
                  "q": Keyword, "key": self.key}
        value = requests.get(url, params=params).json()
        try:
            value["items"]
        except KeyError:
            if value["error"]["errors"][0]["reason"] == "keyInvalid":
                raise errors.WrongAPIKey()
            else:
                eUrl = "https://developers.google.com/youtube/v3/docs/errors"
                raise errors.SearchError(
                    str(value['error']['errors'][0]['reason']) + "\n" + eUrl)
        self.value = value
        r = obj.searched(self.forlist("title"), self.forlist("channelId"),
                         self.forlist("channelTitle"), self.forlist("description"),
                         [i["id"]["kind"] for i in self.value["items"]],
                         [i["id"].get("videoId") for i in self.value["items"]],
                         [i["id"].get("playlistId") for i in self.value["items"]])

        return r

    def forlist(self, flist):
        return [i["snippet"][flist] for i in self.value["items"]]


class nicovideo():
    def search(self, Keyword, Targets=["title", "description", "tags"],
               jsonFilter={}, sort="-viewCounter", Max=5, content="yt-search"):
        url = "https://api.search.nicovideo.jp/api/v2/video/contents/search"
        params = {"q": Keyword, "targets": ",".join(Targets),
                  "fields": "contentId,title,description,userId,viewCounter,mylistCounter,lengthSeconds,thumbnailUrl,startTime,threadId,commentCounter,lastCommentTime,categoryTags,channelId,tags,lockTagsExact,genre",
                  "jsonFilter": json.dumps(jsonFilter),
                  "_sort": sort, "_limit": Max, "_context": content}
        value = requests.get(url, params=params).json()
        if value["meta"]["status"] == 200:
            r = obj.nvsearched([i.get("contentId") for i in value["data"]],
                               [i.get("title") for i in value["data"]],
                               [i.get("description") for i in value["data"]],
                               [i.get("userId") for i in value["data"]],
                               [i.get("viewCounter") for i in value["data"]],
                               [i.get("mylistCounter") for i in value["data"]],
                               [i.get("lengthSeconds") for i in value["data"]],
                               [i.get("thumbnailUrl") for i in value["data"]],
                               [i.get("startTime") for i in value["data"]],
                               [i.get("threadId") for i in value["data"]],
                               [i.get("commentCounter") for i in value["data"]],
                               [i.get("lastCommentTime") for i in value["data"]],
                               [i.get("categoryTags") for i in value["data"]],
                               [i.get("channelId") for i in value["data"]],
                               [i.get("tags") for i in value["data"]],
                               [i.get("lockTagsExact") for i in value["data"]],
                               [i.get("genre") for i in value["data"]])
        else:
            raise errors.SearchError(
                    f"status: {value['meta']['status']},\nerrorCode: {value['meta']['errorCode']},\nerrorMessage: {value['meta']['errorMessage']}")
            return

        return r


class nicolive():
    def search(self, Keyword, Targets=["title", "description", "tags"],
               jsonFilter={}, sort="-viewCounter", Max=5, content="yt-search"):
        url = "https://api.search.nicovideo.jp/api/v2/live/contents/search"
        params = {"q": Keyword, "targets": ",".join(Targets),
                  "fields": "contentId,title,description,userId,channelId,communityId,providerType,tags,categoryTags,viewCounter,commentCounter,openTime,startTime,liveEndTime,timeshiftEnabled,scoreTimeshiftReserved,thumbnailUrl,communityText,communityIcon,memberOnly,liveStatus",
                  "jsonFilter": jsonFilter,
                  "_sort": sort, "_limit": Max, "_context": content}
        value = requests.get(url, params=params).json()
        if value["meta"]["status"] == 200:
            r = obj.nlsearched([i.get("contentId") for i in value["data"]],
                               [i.get("title") for i in value["data"]],
                               [i.get("description") for i in value["data"]],
                               [i.get("userId") for i in value["data"]],
                               [i.get("channelId") for i in value["data"]],
                               [i.get("communityId") for i in value["data"]],
                               [i.get("providerType") for i in value["data"]],
                               [i.get("tags") for i in value["data"]],
                               [i.get("categoryTags") for i in value["data"]],
                               [i.get("viewCounter") for i in value["data"]],
                               [i.get("commentCounter") for i in value["data"]],
                               [i.get("openTime") for i in value["data"]],
                               [i.get("startTime") for i in value["data"]],
                               [i.get("liveEndTime") for i in value["data"]],
                               [i.get("timeshiftEnabled") for i in value["data"]],
                               [i.get("scoreTimeshiftReserved") for i in value["data"]],
                               [i.get("thumbnailUrl") for i in value["data"]],
                               [i.get("communityText") for i in value["data"]],
                               [i.get("communityIcon") for i in value["data"]],
                               [i.get("memberOnly") for i in value["data"]],
                               [i.get("liveStatus") for i in value["data"]])
        else:
            raise errors.SearchError(
                    f"status: {value['meta']['status']},\nerrorCode: {value['meta']['errorCode']},\nerrorMessage: {value['meta']['errorMessage']}")
            return

        return r
