class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def xor(nums):
            total = 0
            for num in nums:
                total ^= num
            return total

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            ans += xor(subset)
                    
        return ans