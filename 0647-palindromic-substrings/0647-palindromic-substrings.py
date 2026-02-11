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
    0 T F F F T
    1   T F T F
    2     T F F
    3       T F
    4         T

    def valid(i, j):
        pass

    '''
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        ans = 0

        def count(l, r):
            ans = 0
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1

                ans += 1
            return ans

        for i in range(n):
            ans += count(i, i) # odd
            ans += count(i, i + 1) # even

        return ans
