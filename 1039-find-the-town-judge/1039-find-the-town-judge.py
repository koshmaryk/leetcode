class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        if not trust:
            return -1

        in_degree = [0] * (n + 1)   # [0,0,0,2]
        out_degree = [0] * (n + 1)  # [0,1,1,0]
        for a,b in trust:
            in_degree[b] += 1
            out_degree[a] += 1

        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        return -1
