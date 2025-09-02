class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}

        res = 0

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if n + 1 in hashmap:
                res = max(res, hashmap[n] + hashmap[n + 1])

            if n - 1 in hashmap:
                res = max(res, hashmap[n] + hashmap[n - 1])

        return res