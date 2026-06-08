import heapq

class KthLargest:
    minHeap = []

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if val >= self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        print(self.minHeap[0])
        return self.minHeap[0]
        
