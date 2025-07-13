class Solution:
    '''
    s = 3[a2[bc]d]ef

    stack = abcbcdabcbcdabcbcdef

    decodedString = 

    k =
    '''
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                decodedString = []
                while stack[-1] != '[':
                   decodedString.append(stack.pop())
                stack.pop() # [
                
                k = 0
                base = 1
                while stack and stack[-1].isdigit():
                    k = k + int(stack.pop()) * base
                    base *= 10

                while k > 0:
                    for i in range(len(decodedString) - 1, -1, -1):
                        stack.append(decodedString[i])
                    k -= 1
                
            else:
                stack.append(c)
        return "".join(stack)