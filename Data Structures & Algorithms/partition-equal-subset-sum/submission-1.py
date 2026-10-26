class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 == 1:
            return False
        else:
            target /= 2
        
        dp = {}

        def explore(curr, i):
            if (curr, i) in dp:
                return dp[(curr, i)]
            if curr > target or (i >= len(nums) and curr != target):
                dp[(curr, i)] = False
                return False
            elif curr == target:
                dp[(curr, i)] = True
                return True
            
            dp[(curr, i)] = explore(curr + nums[i], i + 1) or explore(curr, i + 1)
            return dp[(curr, i)]
        
        return explore(0, 0)
            

        
