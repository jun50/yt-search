from . import errors
import requests
import json


class build():
    def __init__(self, APIKey=None):
        if not APIKey:
            raise errors.MissingAPIKey()
        self.key = APIKey

    def search(self, sKeyword, sMax=5, sType=["video", "channel", "playlist"]):
        value = requests.get(
            f"https://www.googleapis.com/youtube/v3/search?type={','.join(sType)}\
                &maxResults={sMax}&part=snippet&q={sKeyword}&key={self.key}"
                ).json()
        try:
            value["items"]
        except KeyError:
            if value["error"]["errors"][0]["reason"] == "keyInvalid":
                raise errors.WrongAPIKey()
            else:
                raise errors.SearchError(
                    f"{value['error']['errors'][0]['reason']}\n\
                        https://developers.google.com/youtube/v3/docs/errors")
        self.value = value
        r = searched(self.forlist("title"), self.forlist("channelId"),
                     self.forlist("channelTitle"), self.forlist("description"),
                     [i["id"]["kind"] for i in self.value["items"]],
                     [i["id"].get("videoId") for i in self.value["items"]],
                     [i["id"].get("playlistId") for i in self.value["items"]])

        return r

    def forlist(self, flist):
        return [i["snippet"][flist] for i in self.value["items"]]


class searched(object):
    def __init__(self, title, channelId, channelTitle,
                 description, sType, videoId, playlistId):
        self.title = title
        self.channelId = channelId
        self.channelTitle = channelTitle
        self.description = description
        self.sType = sType
        self.videoId = videoId
        self.playlistId = playlistId
