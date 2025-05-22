class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        nums.sort()
        #   |  |  |
        # [-4,-1,-1,0,1,2]
        n = len(nums)
        triplets = []
        for i in range(0, n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r  - 1]:
                        r -= 1
                    
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return triplets
        