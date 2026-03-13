"""

|     |
3,2,1,0,4

|     | |
3,2,1,1,4

| |
2,5,0,0

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastIdx = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= lastIdx:
                lastIdx = i
        return lastIdx == 0
