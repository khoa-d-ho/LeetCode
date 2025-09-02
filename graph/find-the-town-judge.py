class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        
        degree = [0] * n
        for a, b in trust:
            degree[a - 1] -= 1
            degree[b - 1] += 1
        for i in range(1, n+1):
            if degree[i - 1] == n - 1:
                return i
        
        return -1