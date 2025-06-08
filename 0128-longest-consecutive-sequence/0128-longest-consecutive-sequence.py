class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) == 0:
            return ans
        
        nums.sort()

        streak, seq = 0, nums[0]
        i = 0
        while i < len(nums):
            if seq != nums[i]:
                seq = nums[i]
                streak = 0
            
            while i < len(nums) and seq == nums[i]:
                i += 1

            streak += 1
            ans = max(ans, streak)

            seq += 1

        return ans

        # 1,2,3,3,4,100,200
        # 0,1,2,3,4,5,  6
        # seq = 200
        # streak = 1
        # i = 7
        # ans = 4