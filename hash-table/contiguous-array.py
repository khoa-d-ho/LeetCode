class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for item in nums:
            prefix_sum.append(prefix_sum[-1] - (1 if item == 1 else -1))
        
        reference = {}
        max_length = 0
        for i in range(len(prefix_sum)):
            if prefix_sum[i] not in reference:
                reference[prefix_sum[i]] = i
            else:
                max_length = max(i - reference[prefix_sum[i]], max_length)
        
        return max_length