class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followers[userId].add(userId)
        for u in self.followers[userId]:
            l = self.tweet[u]
            minHeap.extend(l)
        heapq.heapify(minHeap)
        while len(res) < 10 and minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
