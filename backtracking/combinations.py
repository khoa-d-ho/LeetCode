class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(curr):
            if len(curr) == k:
                res.append(curr) # pass by reference
                return
            # curr + dfs(curr[-1] + 1)
            #curr = [1]
            #last_number = curr[-1]
            #range(last_number+1, n+1) -> 2, 3, 4
            #? -> curr = [1,2]
            #curr.append(2)
            for next_num in range(curr[-1] + 1, n + 1):
                #curr.append(next_num)
                dfs(curr + [next_num])
                #curr.pop()
            
        for item in range(1, n + 1):
            curr = [item]
            dfs(curr)

        return res