import math

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)

        self.nums = nums
        
        self.size = math.ceil(math.sqrt(n))
        self.blocks = [0] * self.size
        for i in range(n):
            self.blocks[i // self.size] += nums[i]

    def update(self, index: int, val: int) -> None:
        self.blocks[index // self.size] -= self.nums[index]
        self.blocks[index // self.size] += val 
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        s = 0
        start_block = left // self.size
        end_block = right // self.size
        if start_block == end_block:
            for i in range(left, right + 1):
                s += self.nums[i]
        else:
            # partial left block
            for i in range(left, (start_block + 1) * self.size):
                s += self.nums[i]
            # full middle blocks
            for i in range(start_block + 1, end_block):
                s += self.blocks[i]
            # partial right block
            for i in range(end_block * self.size, right + 1):
                s += self.nums[i]
        return s
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)