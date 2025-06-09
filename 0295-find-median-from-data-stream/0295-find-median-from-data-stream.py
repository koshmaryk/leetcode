import heapq

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        if not self.low or -self.low[0] > num:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)

        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low) + 1:
            heapq.heappush(self.low, -heapq.heappop(self.high))


    def findMedian(self) -> flowat:
        if len(self.low) > len(self.high):
            return -self.low[0]
        elif len(self.low) < len(self.high):
            return self.high[0]
        else:
            return (-self.low[0] + self.high[0]) / 2.0
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#
# 1, 4, 6, 7
# low/MaxHeap [3, 2, 1]
# high/MinHeap [4, 6, 7]

# low/MaxHeap [3, 2, 1]
# high/MinHeap [4, 6, 7]