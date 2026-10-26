from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(set)
        maxi = -float('inf')

        for fr, to, p in flights:
            adj[fr].add((to, p))
            if max(fr, to) > maxi:
                maxi = max(fr, to)
        
        queue = []
        heapq.heappush(queue, (0, 0, src))
        # print(adj)
        minCost = []
        for i in range(maxi + 1):
            minCost.append([])
            for j in range(k + 1):
                minCost[i].append(float('inf'))
        minCost[src][0] = 0
        # print(minCost)

        while queue:
            # print(queue)
            cost, i, curr = heapq.heappop(queue)
            # print(queue, cost, i, curr)
            if i > k + 1:
                continue
            if curr == dst:
                return cost

            for nei, p in adj[curr]:
                # print(minCost, nei, i + 1)
                if i + 1 > k and nei != dst:
                    continue
                elif (nei == dst and cost + p > minCost[nei][i]) or (nei != dst and cost + p > minCost[nei][i + 1]):
                    continue
                
                if nei == dst:
                    heapq.heappush(queue, (cost + p, i, nei))
                    minCost[nei][i] = cost + p 
                else:
                    heapq.heappush(queue, (cost + p, i + 1, nei))
                    minCost[nei][i + 1] = cost + p 
            
            # adj[curr] = set()
        
        return -1
        
