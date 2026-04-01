class Solution:
    '''
    s = )()())

    
    01234
    )()()

    2-0=2
    4-0=4

    [0]

    

    '''
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans
