class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if m > n:
            return -1

        for i in range(n - m + 1):
            for j in range(m):
                if needle[j] != haystack[i + j]:
                    break
                if j == m - 1:
                    return i
        return -1
        