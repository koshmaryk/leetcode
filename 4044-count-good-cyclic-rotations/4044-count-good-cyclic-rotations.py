"""
  0 1 2 3  4  5 
  1 2 3 4  5  6
0 1 3 6 10 15 21


123 456 -> 6 15
612 345 -> 9 12
561 234 -> 12 9
456 123 -> 15 6
345 612 -> 12 9
234 561 -> 9 12






"""
class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        h = n // 2

        total = sum(nums)
        p = [0] * (2 * n + 1)
        for i in range(2 * n):
            p[i + 1] = p[i] + nums[i % n]

        ans = 0
        for i in range(n):
            h1 = p[i + h] - p[i]
            if h1 > total - h1:
                ans += 1
        return ans
