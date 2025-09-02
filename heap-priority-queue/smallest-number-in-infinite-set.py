class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.added = []
        self.is_in_added = set()

    def popSmallest(self) -> int:
        if not len(self.added):
            smallest = self.smallest
            self.smallest += 1
        else:
            smallest = heapq.heappop(self.added)
            self.is_in_added.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num >= self.smallest or num in self.is_in_added:
            return
        self.is_in_added.add(num)
        heapq.heappush(self.added, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)