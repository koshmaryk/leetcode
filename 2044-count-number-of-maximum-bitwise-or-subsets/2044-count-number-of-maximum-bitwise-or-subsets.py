class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0

        max_or = 0
        for num in nums:
            max_or |= num

        for mask in range(1 << n):
            curr = 0
            for i in range(n):
                if mask & (1 << i):
                    curr |= nums[i]

            if curr == max_or:
                cnt += 1
        return cnt