from collections import deque

class Logger:

    '''
    dict = x:1; y:5

    x 1 -> true
    x 1 -> 
    y 5 -> true
    x 10 -> false
    x 12 -> true

    '''
    def __init__(self):
        self.messages = deque()
        self.active = set()
        self.window = 10
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        self._cleanup(timestamp)
        if message not in self.active:
            self.active.add(message)
            self.messages.append((message, timestamp))
            return True
        return False

    
    def _cleanup(self, timestamp: int):
        while self.messages and timestamp - self.messages[0][1] >= self.window:
            self.active.remove(self.messages[0][0])
            self.messages.popleft()


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)