from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            values = self.store[key]
            bad, good = -1, len(values)
            while good - bad > 1:
                mid = (bad + good) // 2
                if values[mid][1] > timestamp:
                    good = mid
                else:
                    bad = mid
            return values[bad][0] if values[bad][1] <= timestamp else ""

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)