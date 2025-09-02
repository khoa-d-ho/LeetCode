class Solution:
    def numberCount(self, a: int, b: int) -> int:
        return sum(len(str(i)) == len(set(str(i))) for i in range(a, b+1))