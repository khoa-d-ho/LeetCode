import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Input: trips = [[2,1,5],[3,3,7]], capacity = 5
        # Output: true
        # 1 2 3 4 5 6 7 timeline
        # 2 2 5 5 5 3 3 passengers

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

        seats = capacity - trips[0][0]
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (trips[0][2], trips[0][0]))
        
        for i in range(1, len(trips)):
            p, s, e = trips[i][0], trips[i][1], trips[i][2]
            if s > heap[0][0]:
                seats += heap[0][1]
                heapq.heappop(heap)
            heapq.heappush(heap, (e, p))
            seats -= p
            
            if seats < 0:
                return False
        return True

        

        