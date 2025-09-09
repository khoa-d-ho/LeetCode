import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # When you see "GET TOP K ELEMENTS" your mind should always scream "HEAPQ PROBLEM"
        res_dict = {}
        res = []
        
        for item in items:
            idx, value = item[0], item[1]
            if idx not in res_dict:
                heap = []
                heapq.heapify(heap)
                res_dict[idx] = heap
            heapq.heappush(res_dict[idx], value)
            if len(res_dict[idx]) > 5:
                heapq.heappop(res_dict[idx])
            
        for idx, heap in res_dict.items():
            curr_list = [idx]
            curr_list.append(int(sum(heap) / 5))
            res.append(curr_list)
        res.sort(key = lambda student : student[0])
        return res
            