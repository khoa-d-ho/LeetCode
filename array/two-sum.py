from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            a = target - nums[i]
            if a in d:
                return [i, d[a][0]]

            if nums[i] not in d:
                d[nums[i]] = [i]

            else:
                d[nums[i]].append(i)

        