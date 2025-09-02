class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [float("-inf")]* n
    
        
        for i in range(n):
            dp[i] = matrix[m - 1][i]
            
            
        for row in range(m - 2, -1, -1):
            currentRow = [0] * (n)
            for col in range(n):
                if col == 0:
                    currentRow[col] = min(dp[col], dp[col + 1]) + matrix[row][col]
                elif col == n - 1:
                    currentRow[col] = min(dp[col], dp[col - 1]) + matrix[row][col]
                else:
                    currentRow[col] = min(dp[col], dp[col + 1], dp[col - 1]) + matrix[row][col]
            dp = currentRow
                    
        return min(dp)

