class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        kv = {}
        for i in range(n):
            kv[nums[i]] = i
        for i in range(n):
            diff = target - nums[i]
            if diff in kv and kv[diff] != i:
                return [i, kv[diff]]
        return []