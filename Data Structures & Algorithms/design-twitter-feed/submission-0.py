import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = {}
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
            heapq.heapify(self.posts[userId])

        if userId not in self.followers:
            self.followers[userId] = {userId}
        else:
            self.followers[userId].add(userId)

        heapq.heappush(self.posts[userId], (-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heapsList = []

        if userId in self.followers:
            for followed in self.followers[userId]:
                if self.posts[followed]:
                    heapsList.append(self.posts[followed])
        else:
            return res
        
        # print(heapsList)

        i = 0
        addBack = {}

        while i < 10:
            isEmpty = True
            for heap in heapsList:
                if len(heap):
                    isEmpty = False
                    break
            if isEmpty:
                break
            
            options = []
            for index in range(len(heapsList)):
                if len(heapsList[index]):
                    options.append([heapsList[index][0], index])
            
            # print('o', options)
            currMin, listIndex = min(options, key=lambda x: x[0][0])
            if listIndex not in addBack:
                addBack[listIndex] = {currMin}
            else:
                addBack[listIndex].add(currMin)
            
            res.append(heapq.heappop(heapsList[listIndex])[1])
            i += 1
        
        for index in addBack:
            for element in addBack[index]:
                # print('adding back', index, element)
                heapq.heappush(heapsList[index], element)
        
        # print('addback', addBack)
        # print(userId, res, heapsList)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = {followerId, followeeId}
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print('r', self.posts[followerId])
        self.followers[followerId].remove(followeeId)
        
