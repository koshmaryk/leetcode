"""

2736

7236
2763

"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        n = len(s)
        max_num = num
        for i in range(n):
            for j in range(i + 1, n):
                ls = list(s)
                ls[i], ls[j] = ls[j], ls[i]
                max_num = max(max_num, int("".join(ls)))
        return max_num
        