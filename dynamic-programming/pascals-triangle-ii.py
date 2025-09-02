class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = [[1]]

        for i in range(1, rowIndex + 1):
            row = [1] * (i + 1)
            previous_row = memo[-1]
            for j in range(1, len(previous_row)):
                row[j] = previous_row[j - 1] + previous_row[j]
            memo.append(row)

        return memo[rowIndex]
        