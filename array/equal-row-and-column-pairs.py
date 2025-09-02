class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        rmap = {}
        for r in grid:
            key = ",".join(list(map(str, r)))
            rmap[key] = rmap.get(key, 0) + 1
        print(rmap)
        for c in range(len(grid[0])):
            col = [str(x[c]) for x in grid]
            col = ",".join(col)
            print(col)
            if col in rmap:
                count += rmap[col]
        
        return count