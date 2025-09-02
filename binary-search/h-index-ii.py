class Solution:
    def hIndex(self, citations: List[int]) -> int:
    # 1 2
    #   s
    #   e
    # h = 1
    # mid = 1

        l = len(citations)
        start = 0
        end = len(citations) - 1
        res = 0 
        while start <= end:
            mid = (start + end) // 2
            h = l - mid
            if h > citations[mid]:
                start = mid + 1
            elif h <= citations[mid]:
                end = mid - 1
                res = h
        return res
        