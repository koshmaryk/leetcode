class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        sign = 1

        i = 0
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            sign = 1
            i += 1

        number = 0
        while i < n and s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1

        number *= sign
        if number < -2**31:
            return -2**31
        elif number > 2**31 - 1:
            return 2**31 - 1
        else:
            return number
