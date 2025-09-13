class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr, curr_sum, candidate_idx):
            if curr_sum == target:
                res.append(curr) 
                return
            
            if curr_sum > target:
                return

            for i in range(candidate_idx, len(candidates)):
                dfs(curr + [candidates[i]], curr_sum + candidates[i], i)

        res = []
        for i in range(len(candidates)):
            curr = [candidates[i]]
            dfs(curr, candidates[i], i)

        return res