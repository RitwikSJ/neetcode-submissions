class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_lower = 0
        one_lower = 0

        curr = 2
        while curr <= len(cost):
            two_lower, one_lower = one_lower, min(one_lower + cost[curr - 1], two_lower + cost[curr - 2])
            curr += 1
        
        return one_lower
