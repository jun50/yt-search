class nvsearched(object):
    def __init__(self, contentId, title, description, userId, viewCounter,
                 mylistCounter, lengthSeconds, thumbnailUrl, startTime,
                 threadId, commentCounter, lastCommentTime, categoryTags,
                 channelId, tags, lockTagsExact, genre):
        self.contentId = contentId
        self.title = title
        self.description = description
        self.userId = userId
        self.viewCounter = viewCounter
        self.mylistCounter = mylistCounter
        self.lengthSeconds = lengthSeconds
        self.thumbnailUrl = thumbnailUrl
        self.startTime = startTime
        self.threadId = threadId
        self.commentCounter = commentCounter
        self.lastCommentTime = lastCommentTime
        self.categoryTags = categoryTags
        self.channelId = channelId
        self.tags = tags
        self.lockTagsExact = lockTagsExact
        self.genre = genre


class ytsearched(object):
    def __init__(self, title, channelId, channelTitle,
                 description, sType, videoId, playlistId):
        self.title = title
        self.channelId = channelId
        self.channelTitle = channelTitle
        self.description = description
        self.sType = sType
        self.videoId = videoId
        self.playlistId = playlistId


class nlsearched(object):
    def __init__(self, contentId, title, description, userId, channelId,
                 communityId, providerType, tags, categoryTags,
                 viewCounter, commentCounter, openTime, startTime, liveEndTime,
                 timeshiftEnabled, scoreTimeshiftReserved, thumbnailUrl,
                 communityText, communityIcon, memberOnly, liveStatus):
        self.contentId = contentId
        self.title = title
        self.description = description
        self.userId = userId
        self.channelId = channelId
        self.communityId = communityId
        self.providerType = providerType
        self.tags = tags
        self.categoryTags = categoryTags
        self.viewCounter = viewCounter
        self.commentCounter = commentCounter
        self.openTime = openTime
        self.startTime = startTime
        self.liveEndTime = liveEndTime
        self.timeshiftEnabled = timeshiftEnabled
        self.scoreTimeshiftReserved = scoreTimeshiftReserved
        self.thumbnailUrl = thumbnailUrl
        self.communityText = communityText
        self.communityIcon = communityIcon
        self.memberOnly = memberOnly
        self.liveStatus = liveStatus
