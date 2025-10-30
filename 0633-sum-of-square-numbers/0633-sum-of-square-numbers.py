class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c)) + 1
        s = set()
        for number in range(n):
            s.add(number*number)
            if (c - number*number) in s:
                return True
        return False
        