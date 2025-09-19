class ExamRoom:

    def __init__(self, n: int):
        self.heap = []

    def seat(self) -> int:
        # max heap = (priority, start, end)
        # to pick a seat:
            # take the index that has the highest distance (maxheap)
        # after seating:
            # expand left right
            # fix distance until 
                # 1 2 2 1: you meet index with similar distance that you are trying to fill in
                # 1 2 3 2 1: you meet index with similar distance of the previous index
        
    def leave(self, p: int) -> None:
        

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

# 0 1 2 3 4 5 6 7 8 9 
# x 1 2 1 x 1 2 2 1 x

# heap = [(4, 5, 8), (3, 1, 3)
# pop = (9, 0, 9)
# maxheap?