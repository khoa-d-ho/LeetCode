class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        
        for i in range(1, n):
            min_color = second_min = None
            for c in range(k):
                if min_color is None or costs[i - 1][c] < costs[i - 1][min_color]:
                    second_min = min_color
                    min_color = c
                    
                elif second_min is None or costs[i - 1][c] < costs[i - 1][second_min]:
                    second_min = c
            for color in range(k):
                if color == min_color:
                    costs[i][color] += costs[i - 1][second_min]
                else:
                    costs[i][color] += costs[i - 1][min_color]
            
        return min(costs[n - 1])