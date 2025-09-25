class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for x in range(1, 121):
            for y in range(1, 121):
                if y <= 0.5 * x + 7:
                    continue
                if y > x:
                    continue

                ans += count[x] * count[y]
                if x == y:
                    ans -= count[x]
        return ans
