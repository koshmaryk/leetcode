class MovingAverage:

    '''
    head = 0
    tail = (0 + 1) % 3 = 1; (2 + 1) % 3 = 0; 
    0,0,0

    '''

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = 0
        self.tail = (self.head + 1) % self.size
        self.total = 0
        self.count = 0
        

    def next(self, val: int) -> float:
        self.total -= self.queue[self.tail]
        self.total += val
        self.head = (self.head + 1) % self.size
        self.tail = (self.tail + 1) % self.size
        self.queue[self.head] = val
        self.count += 1
        return self.total / min(self.size, self.count)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)