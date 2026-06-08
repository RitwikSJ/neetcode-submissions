class Solution:
    def canJump(self, nums: List[int]) -> bool:
        closest = len(nums) - 1
        if not closest:
            return True

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= closest - i:
                closest = i
                if i == 0:
                    return True
        
        return False