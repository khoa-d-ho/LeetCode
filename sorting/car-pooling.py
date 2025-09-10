import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Input: trips = [[2,1,5],[3,3,7]], capacity = 5
        # Output: true
        # 1 2 3 4 5 6 7 8  9  10 11 timeline
        # 0 3 3 7 7 3 3 10 10 10 10 passengers
        #  +3  +4       -3+10
        # spots: capacity 0
        # heap = (5, 2) (7, 3)
        # next start = 3
        # next end = 7

        # sort by start time
        # heap first end time
        # loop through: if next start > minheap end:
            # drop off -> leave spots
            # reassign spots number
            # if negative:
                # return
            # heappush (end time, passengers onboard)

        trips.sort(key=lambda k: k[1])
        if trips[0][0] > capacity:
            return False

        total = trips[0][0]
        heap = [(trips[0][2], trips[0][0])]
        heapq.heapify(heap)
        
        # drop off first, pick up later
        for i in range(1, len(trips)):
            print(heap)
            p, s, e = trips[i][0], trips[i][1], trips[i][2]
            while heap:
                if s >= heap[0][0]:
                    total -= heap[0][1]
                    heapq.heappop(heap)
                else:
                    break
            heapq.heappush(heap, (e, p))
            total += p
            
            if total > capacity:
                return False
        return True