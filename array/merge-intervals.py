class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        "Assume an array of video watch times, where each segment 
        represents the times a user started and stopped a video, 
        calculate the total number of unique minutes watched"
        '''
        res = []
        intervals.sort(key=lambda x: x[0])

        for item in intervals:
            if not res or res[-1][1] < item[0]:
                res.append(item)
            else:
                res[-1][1] = max(item[1], res[-1][1])

        return res