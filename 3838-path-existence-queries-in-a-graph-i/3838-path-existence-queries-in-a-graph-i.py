class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        cnt, ccs = 0, [0] * n
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > maxDiff:
                cnt += 1
            ccs[i] = cnt
            

        answer = []
        for u,v in queries:
            answer.append(ccs[u] == ccs[v])
        return answer