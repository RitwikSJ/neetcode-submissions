class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        largest = nums[0]

        for num in nums:
            currSum = max(currSum, 0)
            currSum += num
            if currSum > largest:
                largest = currSum
        
        return largest