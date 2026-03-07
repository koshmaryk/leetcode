"""

3+5/2

"""
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_number = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                curr_number = curr_number * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(curr_number)
                elif op == '-':
                    stack.append(-curr_number)
                elif op == '*':
                    stack.append(stack.pop() * curr_number)
                else:
                    stack.append(int(stack.pop() / curr_number))
                op = c
                curr_number = 0
        
        ans = 0
        while stack:
            ans += stack.pop()
        return ans 
        