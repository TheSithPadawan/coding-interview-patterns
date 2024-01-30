# soln using priority queue for timestamp
# lc link: https://leetcode.com/problems/design-twitter/

class Twitter:

    def __init__(self):
        self.t = 0
        self.user_posts = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        cur_time = self.t
        self.user_posts[userId].append((cur_time, tweetId))
        self.t -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # each user has its priority queue sorted by time
        # when getNewsFeed, print out top 10, exclude the deleted ones
        # <userid: feeds>
        result = []
        minHeap = []

        myPosts = self.user_posts[userId]
        for followee in self.followMap[userId]:
            followeePost = self.user_posts[followee]
            for post in followeePost:
                heapq.heappush(minHeap, post)
        
        for post in myPosts:
            heapq.heappush(minHeap, post)

        while len(result) < 10 and minHeap:
            _, tweetId = heapq.heappop(minHeap)
            result.append(tweetId)
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
