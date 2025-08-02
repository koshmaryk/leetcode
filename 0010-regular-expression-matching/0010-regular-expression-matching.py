class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        def dfs(i, j):
            if j == m:
                return i == n

            matched = i < n and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < m and p[j + 1] == "*": # x*
                return dfs(i, j + 2) or (matched and dfs(i + 1, j))

            if matched:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)
        