from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])
        self._top = None

    def push(self, x: int) -> None:
        self.q2.append(x)
        self._top = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1


    def pop(self) -> int:
        top = self.q1.popleft()
        if self.q1:
            self._top = self.q1[0]
        return top

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
#
# 1 2 3
# 3 1 2
#