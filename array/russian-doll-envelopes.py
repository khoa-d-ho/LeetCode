class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = [1] * len(envelopes)
        envelopes.sort()

        for i in range(1, len(envelopes)):
            wi, hi = envelopes[i]
            max_curr = 1
            for j in range(i):
                wj, hj = envelopes[j]
                if wi > wj and hi > hj:
                    if max_curr < dp[j] + 1:
                        max_curr = dp[j] + 1
            
            dp[i] = max_curr

        return max(dp)    