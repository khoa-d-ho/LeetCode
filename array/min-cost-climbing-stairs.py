class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        take_one_step = 0
        take_two_steps = 0
        min_cost = 0
        for i in range(2, len(cost) + 1):
            temp = take_one_step
            take_one_step = min(take_two_steps + cost[i - 2], take_one_step + cost[i - 1])
            take_two_steps = temp

        return take_one_step