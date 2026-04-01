from collections import deque

class MovingAverage:

    '''
    head = 0
    tail = (0 + 1) % 3 = 1; (2 + 1) % 3 = 0; 
    0,0,0

    '''

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.total = 0
        

    def next(self, val: int) -> float:
        self.window.append(val)
        tail = self.window.popleft() if len(self.window) > self.size else 0
        self.total = self.total - tail + val
        return self.total / len(self.window)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)