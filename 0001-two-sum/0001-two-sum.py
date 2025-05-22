class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        kv = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in kv:
                return [kv[diff], i]
            kv[nums[i]] = i
        return []