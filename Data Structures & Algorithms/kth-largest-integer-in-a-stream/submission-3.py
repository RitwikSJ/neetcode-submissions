import heapq

class KthLargest:
    minHeap = []

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k or val >= self.minHeap[0]:
            heapq.heappush(self.minHeap, val)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
        print(self.minHeap[0])
        return self.minHeap[0]
        
