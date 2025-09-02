class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        max_num = 0
        for i in nums:
            freq[i] += i
            max_num = max(max_num, i)

        def max_points(num):
            if num == 0:
                return 0
            
            if num == 1:
                return freq[1]

            if num not in memo:
                memo[num] = max(max_points(num - 1), max_points(num - 2) + freq[num])

            return memo[num]

        memo = {}
        return max_points(max_num)

        
        
        
        
            
        
                