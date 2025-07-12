class MyQueue:

    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def push(self, x: int) -> None:
        self.enqueue.append(x)

    def pop(self) -> int:
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())
        return self.dequeue.pop()

    def peek(self) -> int:
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())
        return self.dequeue[-1]

    def empty(self) -> bool:
        return not self.enqueue and not self.dequeue
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()