class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        scores = [0] * (n + 1)
        for a, b in trust:
            scores[a] -= 1
            scores[b] += 1

        for i, score in enumerate(scores[1:], 1):
            if score == n - 1:
                return i
        
        return -1