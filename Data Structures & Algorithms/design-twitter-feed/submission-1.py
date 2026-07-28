class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userID: int, tweetID: int) -> None:
        #heapq.heappush([userID, tweetID])
        self.tweetmap[userID].append([self.count, tweetID])
        self.count -= 1

    def getNewsFeed(self, userID: int) -> List[int]:
        res = []
        minheap = []
        self.followmap[userID].add(userID)

        for followeeID in self.followmap[userID]:
            if followeeID in self.tweetmap:
                index = len(self.tweetmap[followeeID]) - 1
                count, tweetID = self.tweetmap[followeeID][index]
                heapq.heappush(minheap, [count, tweetID, followeeID, index - 1])

        while minheap and len(res) < 10:
            count, tweetID, followeeID, index = heapq.heappop(minheap)
            res.append(tweetID)
            if index >= 0:
                count, tweetID = self.tweetmap[followeeID][index]
                heapq.heappush(minheap, [count, tweetID, followeeID, index - 1])
        
        return res

        #for i in range(10):
        #    res.append(userID)
        #
        #return res

    def follow(self, followerID: int, followeeID: int) -> None:
        self.followmap[followerID].add(followeeID)

    def unfollow(self, followerID: int, followeeID: int) -> None:
        if followeeID in self.followmap[followerID]:
            self.followmap[followerID].remove(followeeID)
