class Solution:
    #                    |
    # [0,1,2,3,4,2,2,3,3,4]
    # k = 4
    # i = 7
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
           if nums[i - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k
        