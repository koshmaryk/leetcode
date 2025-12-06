class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            if nums[i] == 0:
                cnt = 0
                while cnt < 3 and i + cnt < n:
                    nums[i + cnt] ^= 1
                    cnt += 1

                if cnt < 3:
                    return -1
                ans +=1
        return ans