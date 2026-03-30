"""


45321
123454321

123544321

345192129

345129921

451299231

451312299


"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1

        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        l, r = i + 1, len(digits) - 1
        while l < r:
            digits[l], digits[r] = digits[r], digits[l]
            l += 1
            r -= 1
        
        number = int("".join(digits))
        return number if number <= 2**31 - 1 else -1
        