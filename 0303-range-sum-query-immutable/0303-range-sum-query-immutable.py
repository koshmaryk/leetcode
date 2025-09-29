class NumArray:
    '''
        0   1  2   3  4
        1, -2, 5, -1, 3

    0   1  -1  4   3  6

    '''

    def __init__(self, nums: List[int]):
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        
        self.p = p

    def sumRange(self, left: int, right: int) -> int:
        return self.p[right + 1] - self.p[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)