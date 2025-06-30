from collections import defaultdict

class Solution:
    # 1,3,2,2,5,2,3,7
    # 1:1, 2:3, 3:2, 5:1, 7:1
    def findLHS(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        ans = 0
        for num in count:
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])
        return ans
