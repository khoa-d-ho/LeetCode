class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost  = 0
        n = len(costs)
        import heapq
        front = costs[:candidates] 
        heapq.heapify(front)
        next_front = candidates

        back = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(back)
        next_back = n - 1 - candidates

        for i in range(k):
            if not back or front and front[0] <= back[0]:
                cost += heapq.heappop(front)

                if next_front <= next_back:
                    heapq.heappush(front, costs[next_front])
                    next_front += 1

            else:
                cost += heapq.heappop(back)

                if next_front <= next_back:
                    heapq.heappush(back, costs[next_back])
                    next_back -= 1
        return cost


        