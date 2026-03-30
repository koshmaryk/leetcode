class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        n = len(nums)

        ans = 1
        cnt = 1
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans