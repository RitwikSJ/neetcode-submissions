import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i].insert(0, points[i][0] ** 2 + points[i][1] ** 2)
        
        heapq.heapify(points)
        res = []

        while len(points) and k:
            res.append(heapq.heappop(points)[1:])
            k -= 1
        
        return res