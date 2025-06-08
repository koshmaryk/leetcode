class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 100,4,200,1,3,2
        # 1,2,3,4,100,200
        # cur_length = 4
        if len(nums) == 0:
            return 0
        nums.sort()
        curr_length, ans = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            elif nums[i - 1] + 1 == nums[i]:
                curr_length += 1
                ans = max(ans, curr_length)
            else:
                curr_length = 1
        return ans