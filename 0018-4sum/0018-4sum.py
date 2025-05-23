class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        output, quadruplet = [], []
        n = len(nums)
        if n < 4:
            return output

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, n - k + 1):
                    if i > start and nums[i - 1] == nums[i]:
                        continue
                    quadruplet.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quadruplet.pop()
                return

            l, r = start, n - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    output.append(quadruplet + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # while l < r and nums[r] == nums[r - 1]:
                    #     r -= 1
        
        kSum(4, 0, target)
        return output