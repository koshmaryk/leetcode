class Solution:
    '''
    s = )()))()()

    i=5

    2-0=2
    4-0=4

    ()())


    ()())))

    '''
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        l, r = 0, 0

        # ())))
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1

            if l == r:
                ans = max(ans, 2 * r)
            if l < r:
                l = r = 0

        l = r = 0
        # (((()
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                l += 1
            else:
                r += 1

            if l == r:
                ans = max(ans, 2 * l)
            elif l > r:
                l = r = 0

        return ans
