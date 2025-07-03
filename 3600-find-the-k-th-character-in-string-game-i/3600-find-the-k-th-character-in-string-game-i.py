class Solution:
    def kthCharacter(self, k: int) -> str:
        s = ['a']
        while len(s) < k:
            size = len(s)
            for i in range(size):
                next_chr = chr(ord('a') + (ord(s[i]) - ord('a') + 1) % 26)
                s.append(next_chr)
        return s[k - 1]
        