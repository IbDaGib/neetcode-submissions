class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.i = 0
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.i, tweetId])
        self.i -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                minheap.append([count, tweetId, followeeId, index-1])
        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index-1])
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
