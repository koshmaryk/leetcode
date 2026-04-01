from collections import deque

class MovingAverage:

    '''
    head = 0
    tail = (0 + 1) % 3 = 1; (2 + 1) % 3 = 0; 
    0,0,0

    '''

    def __init__(self, size: int):
        self.size = size
        self.window = [0] * self.size
        self.head = 0
        self.count = 0
        self.total = 0
        

    def next(self, val: int) -> float:
        tail = (self.head + 1) % self.size
        self.total = self.total - self.window[tail] + val

        self.head = (self.head + 1) % self.size
        self.window[self.head] = val
        self.count += 1

        return self.total / min(self.size, self.count)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)