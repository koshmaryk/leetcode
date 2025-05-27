class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #                   |
        # A D O B E C O D E B A N C
        # |
        # A B C
        #
        m, n = len(s), len(t)
        ans = ""
        if m < n:
            return ans

        count = {}
        for i in range(n):
            count[t[i]] = count.get(t[i], 0) + 1
        
        l = 0
        for r in range(m):
            if s[r] in count:
                count[s[r]] -= 1

            while max(count.values()) <= 0:
                if not ans or r - l + 1 < len(ans):
                    ans = s[l:r+1]
                    
                if s[l] in count:
                    count[s[l]] += 1
                l += 1

        return ans
