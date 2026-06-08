class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dups = {}
        for i in range(len(list)):
            if i == 0:
                non_dups.add(nums[i])
            elif nums[i] in non_dumps:
                return true
        return false
        