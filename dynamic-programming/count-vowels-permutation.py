MOD = 10**9 + 7

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prev = [1] * 5  # 'a', 'e', 'i', 'o', 'u'
        
        for _ in range(1, n):
            # Use only values from `prev` to compute `curr`
            curr = [0] * 5
            curr[0] = prev[1]                     # 'a' follows 'e'
            curr[1] = prev[0] + prev[2]           # 'e' follows 'a' and 'i'
            curr[2] = prev[0] + prev[1] + prev[3] + prev[4]  # 'i' follows all except 'i'
            curr[3] = prev[2] + prev[4]           # 'o' follows 'i' and 'u'
            curr[4] = prev[0]                     # 'u' follows 'a'
            # Update prev for next round
            prev = [x % MOD for x in curr]        # Apply mod here to prevent overflow
        
        return sum(prev) % MOD
