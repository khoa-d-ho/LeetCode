import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, num / -1)
        if len(self.maxheap) - len(self.minheap) > 1 or (self.minheap and self.maxheap and (self.maxheap[0] / -1) > self.minheap[0]):
            heapq.heappush(self.minheap, (heapq.heappop(self.maxheap) / -1)) 
        print("max")
        print(self.maxheap)
        print("min")
        print(self.minheap)
        print(' ')
    def findMedian(self) -> float:
        if len(self.maxheap) - len(self.minheap) == 0:
            return ((self.maxheap[0] / -1) + self.minheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else: 
            return self.maxheap[0] / -1
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# overall: left of median, use max heap to get left middle value (max of right)
         # right of media, use min heap to get right middle value (min of left)
# always add to left. if maxheap > minheap, pop maxheap and push to right (min heap)
# maxheap = [3, 2, 1
# minheap = [4
