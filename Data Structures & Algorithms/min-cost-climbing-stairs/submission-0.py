class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = dict()

        min_cost[0] = 0
        min_cost[1] = 0

        curr = 2
        while curr <= len(cost):
            min_cost[curr] = min(min_cost[curr - 1] + cost[curr - 1], min_cost[curr - 2] + cost[curr - 2])
            curr += 1
        
        return min_cost[len(cost)]
