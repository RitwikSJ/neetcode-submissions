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
        
        if bestL == 0 and bestR != len(nums) - 1:
            r = len(nums) - 1
            curr = maxSum

            while curr > 0 and r > bestR:
                curr += nums[r]
                if curr > maxSum:
                    maxSum = curr
                r -= 1
        elif bestL != 0 and bestR == len(nums) - 1:
            l = 0
            curr = maxSum

            while curr > 0 and l < bestL:
                curr += nums[l]
                if curr > maxSum:
                    maxSum = curr
                l += 1
        
        return maxSum