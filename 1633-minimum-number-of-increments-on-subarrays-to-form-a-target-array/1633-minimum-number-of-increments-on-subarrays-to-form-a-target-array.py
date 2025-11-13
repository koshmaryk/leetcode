class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(n - 1):
            if target[i + 1] > target[i]:
                ans += target[i + 1] - target[i]
        return ans