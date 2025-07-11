class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+':
                x, y = stack[-1], stack[-2]
                stack.append(x + y)
            elif operation == 'D':
                stack.append(stack[-1] * 2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        sum = 0
        while stack:
            sum += stack.pop()
        return sum
