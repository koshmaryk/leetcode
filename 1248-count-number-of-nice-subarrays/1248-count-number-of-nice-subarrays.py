"""
0,1,2,3,4

1,1,2,1,1

odd = 3

l = 1
r = 4

ans = 2

---
k = 2

0,1,2,3,4,5,6,7,8,9

2,2,2,1,2,2,1,2,2,2


at most k:
2,2,2,1,2,2,1
2,2,1,2,2,1
2,1,2,2,1
1,2,2,1

at most k - 1:
2,2,2,1,2,2,1
2,2,1,2,2,1
2,1,2,2,1
1,2,2,1



"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(nums, k):
            n = len(nums)
            ans = odd = l = 0
            for r in range(n):
                odd += nums[r] % 2
                while odd > k:
                    odd -= nums[l] % 2
                    l += 1
                ans += r - l + 1
            print(ans)
            return ans

        return atMost(nums, k) - atMost(nums, k - 1)
