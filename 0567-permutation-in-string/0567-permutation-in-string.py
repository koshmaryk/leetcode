from collections import defaultdict

# ab
# need: a=1, b=1
# window: b=1, a=1
# matches = 0
#
# l = 3, r = 4
# e i d b a o o o
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        for c in s1:
            need[c] += 1

        matches = 0
        window = defaultdict(int)

        l = 0
        for r in range(len(s2)):
            if s2[r] in need:
                window[s2[r]] += 1
                if window[s2[r]] == need[s2[r]]:
                    matches += 1
            
            while r - l + 1 > len(s1):
                if s2[l] in need:
                    if window[s2[l]] == need[s2[l]]:
                        matches -= 1
                    window[s2[l]] -= 1

                l += 1

            if r - l + 1 == len(s1) and matches == len(need):
                return True
        return False