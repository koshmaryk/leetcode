class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #                   |
        # A D O B E C O D E B A N C
        # |
        # A B C
        #
        if t == "" or len(s) < len(t):
            return ""

        window, count = {}, {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        ps, min_len = [-1, -1], 10**5
        have, need = 0, len(count)
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    ps = [l, r]
                    min_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return s[ps[0]:ps[1] + 1] if min_len > 0 else ""

