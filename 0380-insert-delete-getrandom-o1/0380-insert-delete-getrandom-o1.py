import random

class RandomizedSet:

    def __init__(self):
        self.s = []
        self.lookup = {}
        

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False

        self.lookup[val] = len(self.s)
        self.s.append(val)

        return True
        

    def remove(self, val: int) -> bool:
        if val in self.lookup:
            last, idx = self.s[-1], self.lookup[val]
            self.s[idx], self.lookup[last] = last, idx

            self.s.pop()
            del self.lookup[val]
            return True

        return False
        

    def getRandom(self) -> int:
        return random.choice(self.s)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()