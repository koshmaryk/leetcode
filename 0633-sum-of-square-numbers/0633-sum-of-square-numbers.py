class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c ** 0.5)
        while a <= b:
            curr = a * a + b * b
            if curr < c:
                a += 1
            elif curr > c:
                b -= 1
            else:
                return True
        return False