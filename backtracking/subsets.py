class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        binary = []
        x = len(nums)
        for i in range(2**x):
            binary.append(bin(i)[2:].zfill(x)) # add leading 0s
        
        for n in binary:
            temp = []
            for index in range(len(n)):
                if n[index] == "1":
                    temp.append(nums[index])
            result.append(temp)

        return result
                    
            