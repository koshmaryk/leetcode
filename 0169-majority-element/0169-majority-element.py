class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        counter = 0
        for i in range(0, len(nums)):
            if counter == 0:
                candidate = nums[i]
                counter += 1
            elif nums[i] == candidate:
                counter += 1
            else:
                counter -= 1
        return candidate
        