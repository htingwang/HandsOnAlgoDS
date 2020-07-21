class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.friends = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        minheap = []
        for user in self.friends[userId].union(set([userId])):
            for tweet in self.tweets[user]:
                heapq.heappush(minheap, tweet)
                if len(minheap) > 10: heapq.heappop(minheap)

        res = collections.deque()
        while minheap:
            _, tweet = heapq.heappop(minheap)
            res.appendleft(tweet)
        return list(res)

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.friends[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.friends[followerId]: self.friends[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
