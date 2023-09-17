class Solution:
    def firstUniqChar(self, s: str) -> int:
        counters = collections.Counter(s)
        for i, ch in enumerate(s):
            if counters[ch] == 1:
                return i
        return -1
