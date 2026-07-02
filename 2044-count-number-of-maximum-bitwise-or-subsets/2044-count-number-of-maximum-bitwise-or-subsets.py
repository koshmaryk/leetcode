class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0

        max_or = 0
        for num in nums:
            max_or |= num

        def gen(i, curr):
            nonlocal cnt
            if i == n:
                if curr == max_or:
                    cnt += 1
                return

            gen(i + 1, curr | nums[i])
            gen(i + 1, curr)
            

        gen(0, 0)
        return cnt