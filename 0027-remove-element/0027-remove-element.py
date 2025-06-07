class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2,2,3,2,3
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
