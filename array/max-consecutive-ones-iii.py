class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 1,1,1,0,0,0,1,1,1,1,0 k = 2
        # s
        #           e
        # 3
        res = 0
        flipped = 0
        start = 0
        end = 0

        while end < len(nums):
            if nums[end] == 0:
                flipped += 1

            if flipped > k: 
                if nums[start] == 0:
                    flipped -= 1
                start += 1
            end += 1
        
        return end - start


                    
                    
        
                        

                    
            


                
