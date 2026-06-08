class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        withoutPrev = nums[0]
        withPrev = max(nums[0], nums[1])
        
        for i in range(2, len(nums) - 1):
            withoutPrev, withPrev = withPrev, max(withoutPrev + nums[i], withPrev)

        option1 = max(withoutPrev, withPrev)

        withoutPrev = nums[1]
        withPrev = max(nums[1], nums[2])
        
        for i in range(3, len(nums)):
            withoutPrev, withPrev = withPrev, max(withoutPrev + nums[i], withPrev)
        
        return max(option1, withoutPrev, withPrev)
        