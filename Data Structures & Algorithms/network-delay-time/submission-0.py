import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortestPath = dict()
        adjList = dict()
        visited = set()

        for v in range(1, n + 1):
            if v == k:
                shortestPath[v] = 0
            else:
                shortestPath[v] = None
            adjList[v] = []
        
        for e in times:
            adjList[e[0]].append(e[1:])
        
        nodes = [(0, k)]
        heapq.heapify(nodes)

        while len(visited) != n and nodes:
            dist, currNode = heapq.heappop(nodes)
            if currNode in visited:
                continue
            visited.add(currNode)

            for nei, w in adjList[currNode]:
                if shortestPath[nei] is None:
                    shortestPath[nei] = w + dist
                    heapq.heappush(nodes, (shortestPath[nei], nei))
                elif w + dist < shortestPath[nei]:
                    shortestPath[nei] = w + dist
                    heapq.heappush(nodes, (shortestPath[nei], nei))
        
        maxDist = -1
        
        for dist in shortestPath.values():
            if dist is None:
                return -1
            maxDist = max(maxDist, dist)
        
        return maxDist

        