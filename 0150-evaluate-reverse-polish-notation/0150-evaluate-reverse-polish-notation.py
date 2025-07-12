class Solution:
    '''
    "2","1","+","3","*"




    '''
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                y, x = stack.pop(), stack.pop()
                stack.append(x + y)
            elif token == "-":
                y, x = stack.pop(), stack.pop()
                stack.append(x - y)
            elif token == "*":
                y, x = stack.pop(), stack.pop()
                stack.append(x * y)
            elif token == "/":
                y, x = stack.pop(), stack.pop()
                stack.append(int(x / y))
            else:
                stack.append(int(token))
        return stack.pop()
