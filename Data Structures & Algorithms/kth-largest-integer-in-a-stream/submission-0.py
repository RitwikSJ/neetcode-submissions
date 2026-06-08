import heapq

class KthLargest:
    minHeap = []

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        for i in range(len(nums) - 1, len(nums) - 1 - k, -1):     
            heapq.heappush(self.minHeap, nums[i])

    def add(self, val: int) -> int:
        print(self.minHeap[0])
        if val >= self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
        
