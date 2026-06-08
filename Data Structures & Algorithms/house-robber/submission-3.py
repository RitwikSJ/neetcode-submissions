class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        withPrev = nums[1]
        withoutPrev = nums[0]
        
        for i in range(2, len(nums)):
            withPrev, withoutPrev = max(withoutPrev + nums[i], withPrev), withPrev
        
        return withPrev
        