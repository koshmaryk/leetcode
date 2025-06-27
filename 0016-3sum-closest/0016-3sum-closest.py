class Solution:
    # nums = [-1,2,1,-4], target = 1
    # i = -1, sum = -3, diff = 4
    #
    # i = -1, sum = 2, diff = -1 
    # 
    # i = 2, sum = -1, diff = 
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        diff = float('inf')
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(target - sum) < abs(diff):
                    diff = target - sum

                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return sum
        return target - diff