class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        studs = {}
        import heapq
        for i, score in items:
            studs[i] = studs.get(i, [])
            heapq.heappush(studs[i], -score)

        solution = []
        for i in sorted(studs.keys()): 
            top_five = [-heapq.heappop(studs[i]) for _ in range(5)]
            average = sum(top_five) // 5
            solution.append([i, average])
        return solution