from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.values = deque([])
        

    def next(self, val: int) -> float:
        self.values.append(val)
        if len(self.values) > self.size:
            self.values.popleft()

        return sum(self.values) / min(len(self.values), self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)