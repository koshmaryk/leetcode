"""

0,0
1,3
2,5
3,7


"""
import bisect
from math import inf


class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.elements = [[(0,0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        if self.elements[index][-1][0] == self.id:
            self.elements[index].pop()
            
        self.elements[index].append((self.id, val))
        

    def snap(self) -> int:
        self.id += 1
        return self.id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.elements[index], (snap_id, inf))
        return self.elements[index][i - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)