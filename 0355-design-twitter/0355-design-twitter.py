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
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        
        tweets = []
        tweets.extend(self.users[userId].tweets)
        for followeeId in self.users[userId].followees:
            tweets.extend(self.users[followeeId].tweets)
        tweets.sort(key=lambda tweet: tweet.timestamp, reverse=True)
        
        news_feed = []
        i = 0
        while i < len(tweets):
            news_feed.append(tweets[i].id)
            i += 1
            if len(news_feed) == 10:
                break
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