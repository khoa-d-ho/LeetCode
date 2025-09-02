class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # new_intervals = [(2, [1, 2]), (1, [2, 3]), (0, [3, 4])]
        #                       s                        e
        # mid = 1
        # target_end = 2
        # need to find [2,3] with 2 being target
        def binary_search(target_end, new_intervals):
            start = 0
            end = len(new_intervals) - 1
            res = -1
            while start <= end:
                mid = (start + end) // 2
                mid_index = new_intervals[mid][0]
                mid_start = new_intervals[mid][1][0]
        
                if mid_start >= target_end:
                    res = mid_index
                    end = mid - 1
                else: 
                    start = mid + 1
            return res
            
        new_intervals = sorted(enumerate(intervals), key = lambda interval: interval[1])
        ans = []
        for original_index, interval in enumerate(intervals):
            target_end = interval[1]
            ans.append(binary_search(target_end, new_intervals)) 
        return ans

        
            
            