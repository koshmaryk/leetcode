class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def xor(nums):
            total = 0
            for num in nums:
                total ^= num
            return total

        def gen(start, prefix):
            nonlocal ans
            ans += xor(prefix)
            for i in range(start, n):
                prefix.append(nums[i])
                gen(i + 1, prefix)
                prefix.pop()

        gen(0, [])
        return ans