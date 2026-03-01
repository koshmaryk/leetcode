"""

    aababbabb

    bbbbb

count_a = 0
ans = 3

count_b = 5




"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a = s.count('a')
        count_b = 0
        ans = count_a
        for c in s:
            if c == 'a':
                count_a -= 1
            if c == 'b':
                count_b += 1
            ans = min(ans, count_a + count_b)
        return ans