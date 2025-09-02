class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(self.grid)
        self.value_dict = {}
        
        for r in range(self.n):
            for c in range(self.n):
                value = self.grid[r][c]
                self.value_dict[value] = (r, c)

    def adjacentSum(self, value: int) -> int:
        adj_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        r, c = self.value_dict[value]
        total = 0
        for dr, dc in adj_moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total += self.grid[nr][nc]
        return total

    def diagonalSum(self, value: int) -> int:
        dia_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        r, c = self.value_dict[value]
        total = 0
        for dr, dc in dia_moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total += self.grid[nr][nc]
        return total

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(self.grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)