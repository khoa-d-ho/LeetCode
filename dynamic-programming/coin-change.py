class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coins = [1,2,5], amount = 11
        dp[i] stores min coins needed to create i dollars
        dp[i] = min(1 + dp[i - c]) for c in [1,2,5], and for c <= current amt
              1 2 3 4 5 6 7 8 9 1011
        dp=[0,1,1,2,2,1,4,x,x,x,x,x]
        dp0 = 0   1 here is for the 1,2,5 coin that you are trying to add 
        dp1 = 1   v
        dp2 = min(1 + dp[2-1]) = min(dp[1]) = 1
        dp3 = min(1 + dp[3-2, 3-1]) = min dp1, dp2 = 1
        ...
        dp6 = min(1 + dp[6-1, 6-2, 6-5]) = min(1 + dp[5,4,1]) = 1 + dp5 = 2
        dp7 = min(1 + dp[6,5,2]) = 1 + dp5 = 2
        ...
        '''
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            min_curr = amount + 1 # max it can go
            for coin in coins:
                if coin <= i: # equal because can use coin again
                    if min_curr > dp[i-coin] + 1:
                        min_curr = dp[i-coin] + 1
            dp[i] = min_curr # dont +1 here, wrong signal
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]