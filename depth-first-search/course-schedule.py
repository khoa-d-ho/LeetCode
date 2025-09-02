class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        node_visited = 0
        while queue:
            node = queue.popleft()
            node_visited += 1
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
            

        return node_visited == numCourses