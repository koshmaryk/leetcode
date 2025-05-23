class Solution:
    # [1,0,-1,0,-2,2]
    #
    #        | | | |
    # [-2,-1,0,0,1,2]
    # a = 1
    # b = 2
    # c = 3
    # d = 5
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        n = len(nums)
        if n < 4:
            return output

        nums.sort()
        for a in range(n - 3):
            if a > 0 and nums[a - 1] == nums[a]:
                    continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue
                c, d = b + 1, n - 1
                while c < d:
                    current_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if current_sum == target:
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                            
                        output.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                    elif current_sum > target:
                        d -= 1
                    else:
                        c += 1
        
        return output

