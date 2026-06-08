class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l = 0
        r = 0
        bestL, bestR = 0, 0
        curr = 0
        maxSum = -30001

        while r <= len(nums) - 1:
            curr += nums[r]
            if curr > maxSum:
                bestL = l
                bestR = r
                maxSum = curr
            if curr < 0:
                l = r + 1
                curr = 0
                        
            r += 1
        
        print(bestL, bestR)
        
        # if bestL != 0 and bestR != len(nums) - 1:
        #     return maxSum
        
        l = 0
        r = 0
        bestL, bestR = None, None
        curr = 0
        minSum = 30001

        while r <= len(nums) - 1:
            curr += nums[r]

            if curr < minSum:
                minSum = curr
                bestL = l
                bestR = r
            if curr > 0:
                l = r + 1
                curr = 0
            
            r += 1

        if bestL == 0 and bestR == len(nums) - 1:
            return maxSum

        return max(sum(nums) - minSum, maxSum)