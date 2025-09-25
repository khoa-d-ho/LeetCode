class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 116
        # 122
        n = len(candidates)
        res = []
        candidates.sort()

        def backtrack(first, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])

            for i in range(first, n):
                if i > first and candidates[i] == candidates[i-1]:
                    continue

                curr.append(candidates[i])
                backtrack(i + 1, curr, curr_sum + candidates[i])
                curr.pop()
        backtrack(0, [], 0)
        return res