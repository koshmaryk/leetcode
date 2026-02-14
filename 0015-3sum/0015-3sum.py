class Solution:
    '''
    0,2,3
    -2,0,5,-3,7

    -3,-2,0,5,7

    -3,-2,-2,0,5,5

    -3,-2,5
    [0,1,5], [0,2,4]

    i=0
    nums[i] = -3

    l=i+1; r=n-1

    1) nums[i] + nums[j] + nums[k] == 0
    2) nums[i] + nums[j] + nums[k] > 0 r -= 1
    2) nums[i] + nums[j] + nums[k] < 0 l += 1



    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()
        triplets = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return triplets