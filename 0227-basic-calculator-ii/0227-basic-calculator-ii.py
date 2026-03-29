"""

+3+5/2+10

op = +
number = 10

iter = 0

stack = 15

"""
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        number = 0
        for i, c in enumerate(s):
            if c.isdigit():
                number = number * 10 + int(c)

            if c in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(number)
                elif op == "-":
                    stack.append(-number)
                elif op == "*":
                    stack.append(stack.pop() * number)
                else:
                    stack.append(int(stack.pop() / number))

                op = c
                number = 0

        ans = 0
        while stack:
            ans += stack.pop()
        return ans
        