import heapq

class User:
    def __init__(self, id: int):
        self.id = id
        self.followees = set()
        self.tweets = []
        
class Tweet:
    def __init__(self, id: int, timestamp: int):
        self.id = id
        self.timestamp = timestamp
        
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.users = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.users.get(userId, User(userId))
        user.tweets.append(Tweet(tweetId, self.timestamp))
        self.timestamp += 1
        self.users[userId] = user
        

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.users:
            return []
        
        tweets = []
        for tweet in self.users[userId].tweets[-10:]:
            heapq.heappush(tweets, (-tweet.timestamp, tweet.id))
        
        for followeeId in self.users[userId].followees:
            for tweet in self.users[followeeId].tweets[-10:]:
                heapq.heappush(tweets, (-tweet.timestamp, tweet.id))
        
        news_feed = []
        while tweets and len(news_feed) < 10:
            news_feed.append(heapq.heappop(tweets)[1])
        return news_feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
        
        follower = self.users.get(followerId, User(followerId))
        followee = self.users.get(followeeId, User(followeeId))          
        follower.followees.add(followeeId)
        
        self.users[followerId] = follower
        self.users[followeeId] = followee
        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
        
        follower = self.users.get(followerId, User(followerId))
        if followeeId in follower.followees:
            follower.followees.remove(followeeId)
        self.users[followerId] = follower