from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            counter = defaultdict(int)
            for j in range(i, n):
                counter[s[j]] += 1
                if len(set(counter.values())) == 1:
                    ans = max(ans, j - i + 1)
        return ans