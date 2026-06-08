class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0

        while r != len(nums) - 1:
            steps += 1

            for i in range(l, r + 1):
                r = max(r, i + nums[i])
            if r >= len(nums) - 1:
                break
            l += 1
            
        return steps
            
            