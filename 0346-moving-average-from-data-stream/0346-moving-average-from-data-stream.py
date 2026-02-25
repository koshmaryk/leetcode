from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque([])
        self.window = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        tail = self.queue.popleft() if len(self.queue) > self.size else 0
        self.window = self.window - tail + val
        return self.window / min(len(self.queue), self.size)
       


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)