# s1Count = 1 1 0 0 0 ... 0 ...
# s2Count = 1 1 0 0 0 ... 0 ...
# matches == 26
# ab
# 
# e i d b a o o o
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(n1, n2):
            if matches == 26:
                return True

            i = ord(s2[r]) - ord('a')
            s2Count[i] += 1
            if s1Count[i] == s2Count[i]:
                matches += 1
            elif s1Count[i] + 1 == s2Count[i]:
                matches -= 1

            i = ord(s2[l]) - ord('a')
            s2Count[i] -= 1
            if s1Count[i] == s2Count[i]:
                matches += 1
            elif s1Count[i] - 1 == s2Count[i]:
                matches -= 1
            l += 1

        return matches == 26
