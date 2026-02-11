class Solution:
    '''
    "aaa" 3 + 1 + 1 => a, a, a, aa, aa, aaa
    "aba" 3 + 1 => a, b, a, aba
    "abcba" 5 + 1 + 1 => a, b, c, b, a, bcb, abcba

    0,n-1
    1,n-1; 0,n-2

    xabcbax

    c
    bcb
    abcba
    xabcbax

    abcba
      0 1 2 3 4
      a b c b a
    0 T F F F F
    1   T F T F
    2     T F F
    3       T F
    4         T

    def valid(i, j):
        pass

    '''
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = 0

        # base case: substr of len 1
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # base case: substr of len 2
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            ans += int(dp[i][i + 1])

        # length=3
        # i=0; j=i+3-1=2
        # i=1; j=i+3-1=3
        # ...
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                ans += int(dp[i][j])

        return ans
