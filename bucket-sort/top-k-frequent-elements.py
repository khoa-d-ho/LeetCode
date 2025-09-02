class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for item in nums:
            if item not in freq_dict:
                freq_dict[item] = 1
            else: 
                freq_dict[item] += 1

        heap = []
        for key, value in freq_dict.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for value, key in heap:
            res.append(key)
        
        return res

