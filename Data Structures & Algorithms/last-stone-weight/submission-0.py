class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for i in range(len(stones)):
            heapq.heappush(maxHeap, -stones[i])
        
        while len(maxHeap) > 1:
            stoneA = heapq.heappop(maxHeap)
            stoneB = heapq.heappop(maxHeap)

            if stoneA > stoneB:
                heapq.heappush(maxHeap, stoneB - stoneA)
            elif stoneA < stoneB:
                heapq.heappush(maxHeap, stoneA - stoneB)

        if len(maxHeap) != 0:
            return -maxHeap[0]
        
        return 0