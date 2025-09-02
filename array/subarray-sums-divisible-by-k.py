class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 4 5 0 -2 -3 1
    #   0 4 9 9  7  4 5
    #   0 4 4 4  2  4 0
        ans = 0
        d = {0:1}
        curr = 0
        prefix_sum = [0]
        curr_sum = 0
        for item in nums:
            prefix_sum.append(curr_sum + item)
            curr_sum = prefix_sum[-1]
            curr_mod = curr_sum % k
            if curr_mod not in d:
                d[curr_mod] = 1
            else:
                ans += d[curr_mod]
                d[curr_mod] += 1
        return ans

            


