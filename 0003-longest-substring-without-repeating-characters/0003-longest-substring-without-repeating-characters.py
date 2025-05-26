from collections import defaultdict

class Solution:
    # |     |
    # a b c a b c b b
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
                    
        return ans
            
