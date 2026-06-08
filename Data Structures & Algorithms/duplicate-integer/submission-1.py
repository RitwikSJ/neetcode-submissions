class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dups = set()
        for i in range(len(nums)):
            if i == 0:
                non_dups.add(nums[i])
            elif nums[i] in non_dups:
                return True
            else:
                non_dups.add(nums[i])
        return False
        