# yt-search

## English

## Install

**Python 3.6.x or higher is required.**

Install command:

```cmd
# Linux/OS X
$ python -m pip install -U yt-search

# Windows
> py -3 -m pip install -U yt-search
```

## Example

Search video

```python
import yt_search

yt = yt_search.build("API Key")
search_result = yt.search("keyword", sMax=10, sType=["video"])
print(search_result.title)
print(search_result.videoId)
print(search_result.channelTitle)
```

Search YouTube channel

```python
import yt_search

yt = yt_search.build("API Key")
search_result = yt.search("keyword", sMax=10, sType=["channel"])
print(search_result.channelTitle)
print(search_result.channelId)
```

Search playlist

```python
import yt_search

yt = yt_search.build("API Key")
search_result = yt.search("keyword", sMax=10, sType=["playlist"])
print(search_result.title)
print(search_result.playlistId)
print(search_result.channelTitle)
```

sType can be select multiple by list

```python
import yt_search

yt = yt_search.build("API Key")
search_result = yt.search("keyword", sMax=10, sType=["video", "playlist"])
print(search_result.title)
print(search_result.videoId)
print(search_result.playlistId)
print(search_result.channelTitle)
```

Download search results with wav

Need youtube-dl and ffmpeg.

```python
import yt_search
import youtube_dl

yt = yt_search.build("API Key")
search_result = yt.search("keyword", sMax=10, sType=["video"])

options = {
    'format': 'bestaudio/bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        },
        {
            'key': 'FFmpegMetadata'
        }
    ]
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=" + i
                  for i in search_result.videoId])
```

In the case of youtube#video, playlistId returns None.
In the case of youtube#playlist, videoId returns None.
In the case of youtube#channel, playlistId and videoId returns None.

## 日本語

## インストール

**Python3.6.x以上が必要です。**

インストールコマンド：

```cmd
# Linux/OS X
$ python -m pip install -U yt-search

# Windows
> py -3 -m pip install -U yt-search
```

## プログラムの例

動画を検索

```python
import yt_search

yt = yt_search.build("APIキー")
search_result = yt.search("キーワード", sMax=10, sType=["video"])
print(search_result.title)
print(search_result.videoId)
print(search_result.channelTitle)
```

YouTubeチャンネルを検索

```python
import yt_search

yt = yt_search.build("APIキー")
search_result = yt.search("キーワード", sMax=10, sType=["channel"])
print(search_result.channelTitle)
print(search_result.channelId)
```

プレイリストを検索

```python
import yt_search

yt = yt_search.build("APIキー")
search_result = yt.search("キーワード", sMax=10, sType=["playlist"])
print(search_result.title)
print(search_result.playlistId)
print(search_result.channelTitle)
```

sTypeはリストで複数選択可能です。例：

```python
import yt_search

yt = yt_search.build("APIキー")
search_result = yt.search("キーワード", sMax=10, sType=["video", "playlist"])
print(search_result.title)
print(search_result.videoId)
print(search_result.playlistId)
print(search_result.channelTitle)
```

検索結果をwavでダウンロード

youtube-dlとffmpegが必要です。

```python
import yt_search
import youtube_dl

yt = yt_search.build("APIキー")
search_result = yt.search("キーワード", sMax=10, sType=["video"])

options = {
    'format': 'bestaudio/bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        },
        {
            'key': 'FFmpegMetadata'
        }
    ]
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=" + i
                  for i in search_result.videoId])
```

youtube#videoの場合はplaylistIdが、
youtube#playlistの場合はvideoIdが、
youtube#channelの場合はplaylistIdとvideoIdがNoneを返します。
Noneを返さない場合もあります（値があるとき）
