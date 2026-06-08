class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l = 0
        r = 1
        bestL, bestR = 0, 0
        curr = nums[0]
        maxSum = curr

        while r <= len(nums) - 1:
            curr += nums[r]
            if curr < 0:
                l = r + 1
                curr = 0
            elif curr > maxSum:
                bestL = l
                bestR = r
                maxSum = curr
            
            r += 1
        
        if bestL != 0 and bestR != len(nums) - 1:
            return maxSum
        
        l = 0
        r = 1
        curr = nums[0]
        minSum = curr

        while r <= len(nums) - 1:
            curr += nums[r]
            if curr > 0:
                l = r + 1
                curr = 0
            elif curr < maxSum:
                minSum = curr
            
            r += 1
        
        return sum(nums) - minSum