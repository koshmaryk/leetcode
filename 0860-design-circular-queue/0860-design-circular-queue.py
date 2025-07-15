class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k + 1
        self.arr = [0] * (k + 1)
        self.head = 0
        self.tail = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.tail - 1) % self.capacity]
        

    def isEmpty(self) -> bool:
        return self.getSize() == 0

    def isFull(self) -> bool:
        return self.getSize() == self.capacity - 1

    def getSize(self) -> int:
        if self.head > self.tail:
            return self.capacity - self.head + self.tail
        return self.tail - self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()