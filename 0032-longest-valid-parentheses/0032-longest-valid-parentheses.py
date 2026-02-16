class Solution:
    '''
    s = )()())

    i=5

    2-0=2
    4-0=4

    5
    

    '''
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else: # )
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans
