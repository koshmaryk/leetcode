class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        cnt = 0
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    cnt += k - j
                    j += 1
                else:
                    k -= 1
        return cnt