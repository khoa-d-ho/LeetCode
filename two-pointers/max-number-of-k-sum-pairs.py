class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        complement = {}
        count = 0
        for i in nums:
            comp = k - i
            if comp in complement and complement[comp] > 0:
                count += 1
                complement[comp] -= 1
            else:
                complement[i] = complement.get(i, 0) + 1
        print(complement)
        return count