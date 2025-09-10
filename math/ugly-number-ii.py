import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:     
        # create ugly nums using heap
        # init heap with 1
        # pop, then mult by 2, 3, 5
        # do the same
        # number popped at nth time is res

        heap = [1]
        heapq.heapify(heap)

        primes = [2, 3, 5]
        for i in range(n):
            curr = heapq.heappop(heap)
            for prime in primes:
                new = prime * curr
                if new not in heap:
                    heapq.heappush(heap, prime * curr)
        
        return curr

        