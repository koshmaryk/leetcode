class MovingAverage:

    '''
    head = 0
    tail = (0 + 1) % 3 = 1; (2 + 1) % 3 = 0; 
    0,0,0

    '''

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.window = 0
        self.head = 0
        self.tail = (self.head + 1) % self.size
        self.count = 0
        

    def next(self, val: int) -> float:
        self.window = self.window - self.queue[self.tail] + val
        self.head = (self.head + 1) % self.size
        self.tail = (self.head + 1) % self.size
        self.queue[self.head] = val
        self.count += 1
        return self.window / min(self.size, self.count)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)