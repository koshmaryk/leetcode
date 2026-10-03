"""
  0 1 2 3  4  5 
  1 2 3 4  5  6
0 1 3 6 10 15 21 22 24 27 31 36 42


123 456 -> 6 15
612 345 -> 9 12
561 234 -> 12 9
456 123 -> 15 6
345 612 -> 12 9
234 561 -> 9 12


0 1 2 3 4 5
1 2 3 4 5 6

"""
class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        h = n // 2

        total = sum(nums)
        p = sum(nums[:h])

        ans = 0
        for i in range(n):
            if 2 * p > total:
                ans += 1
            p -= nums[i]
            p += nums[(i + h) % n]
        return ans
