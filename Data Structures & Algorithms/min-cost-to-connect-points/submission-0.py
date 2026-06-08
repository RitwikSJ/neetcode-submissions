import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(pt1, pt2):
            return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

        points = [tuple(x) for x in points]
        
        adjList = dict()
        for i in range(len(points)):
            adjList[points[i]] = []

        for i in range(len(points)):
            for j in range(i, len(points)):
                manDist = dist(points[i], points[j])
                # adjList[points[i]].append([manDist, points[i], points[j]])
                # adjList[points[j]].append([manDist, points[j], points[i]])
                adjList[points[i]].append([manDist, points[j]])
                adjList[points[j]].append([manDist, points[i]])
        
        heap = adjList[points[0]]
        heapq.heapify(heap)
        visited = {points[0]}

        total = 0

        while heap:
            w, nei = heapq.heappop(heap)

            if nei in visited:
                continue
            
            visited.add(nei)
            total += w
            for edge in adjList[nei]:
                heapq.heappush(heap, edge)
        
        return total

