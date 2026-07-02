class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0

        max_or = 0
        for num in nums:
            max_or |= num

        memo = {}
        def count(i, curr):
            if i == n:
                return 1 if curr == max_or else 0

            if (i, curr) in memo:
                return memo[(i, curr)]

            memo[(i, curr)] = count(i + 1, curr | nums[i]) + count(i + 1, curr)
            return memo[(i, curr)]

        return count(0, 0)