class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # skip adjacent
        new = []
        curr_num = None
        for item in nums:
            if curr_num != item:
                new.append(item)
                curr_num = item
        
        res = 0
        status = 0
        curr = 0
        for i in range(1, len(new) - 1):
            if new[i-1] > new[i] and new[i+1] > new[i]:
                curr = -1 # valley
            elif new[i-1] < new[i] and new[i+1] < new[i]:
                curr = 1 # hill
            
            if curr != status:
                status = curr
                res += 1
        return res
                
