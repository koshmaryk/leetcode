import heapq

class MedianFinder:

    def __init__(self):
        self.H_Low = []
        self.H_High = []
        

    def addNum(self, num: int) -> None:
        if not self.H_Low and not self.H_High:
            heapq.heappush(self.H_Low, -num)
        elif self.H_Low and -self.H_Low[0] > num:
            heapq.heappush(self.H_Low, -num)
        else:
            heapq.heappush(self.H_High, num)

        if len(self.H_Low) - len(self.H_High) > 1:
            heapq.heappush(self.H_High, -heapq.heappop(self.H_Low))
        elif len(self.H_High) - len(self.H_Low) > 1:
            heapq.heappush(self.H_Low, -heapq.heappop(self.H_High))


    def findMedian(self) -> float:
        if len(self.H_Low) > len(self.H_High):
            return -self.H_Low[0]
        elif len(self.H_Low) < len(self.H_High):
            return self.H_High[0]
        else:
            return (-self.H_Low[0] + self.H_High[0]) / 2.0
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#
# 1, 4, 6, 7
# H_Low/MaxHeap [3, 2, 1]
# H_High/MinHeap [4, 6, 7]

# H_Low/MaxHeap [3, 2, 1]
# H_High/MinHeap [4, 6, 7]