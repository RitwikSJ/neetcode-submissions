import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, i)
            elif i > min_heap[0]:
                heapq.heappush(min_heap, i)
                heapq.heappop(min_heap)

        return min_heap[0]

