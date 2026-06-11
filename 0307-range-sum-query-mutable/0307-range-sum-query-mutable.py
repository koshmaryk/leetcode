"""
[1,3,5,7] = 4

16,4,12,|1,3,5,7

[1,2] -> 8
lo=5
hi=7

"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)

        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        

    def update(self, index: int, val: int) -> None:
        i = self.n + index
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        

    def sumRange(self, left: int, right: int) -> int:
        lo, hi = self.n + left, self.n + right + 1 # half-open [lo,hi)
        s = 0
        while lo < hi:
            if lo & 1:
                s += self.tree[lo]
                lo +=1

            if hi & 1:
                hi -= 1
                s += self.tree[hi]

            lo >>= 1
            hi >>= 1
        return s

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)