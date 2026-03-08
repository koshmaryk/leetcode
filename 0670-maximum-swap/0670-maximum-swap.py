"""

2736

7236
2763

"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)

        last = {}
        for i in range(n):
            last[s[i]] = i

        for i in range(n):
            for digit in range(9, int(s[i]), -1):
                if str(digit) in last and last[str(digit)] > i:
                    j = last[str(digit)]
                    s[i], s[j] = s[j], s[i]
                    return int("".join(s))
        return num
        