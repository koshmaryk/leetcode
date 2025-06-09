class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #
        #   1,2,3 k = 3
        # 0 1 3 6
        #
        #   1 -1 1 -1 0 k = 0
        # 0 1  0 1  0 0
        #
        #   1 2 -1 -1 k = 1
        # 0 1 3  2  1
        # 
        # k= 5; p = 50, -3 2 1 4 1 0

        n = len(nums)
        ans = 0 # 2

        p = 0 # 3
        count = {0: 1} # 1:1; 3:1; 6:1
        for i in range(n):
            p += nums[i] # 1; 3; 6
            if p - k in count:
                ans += count[p - k]
            count[p] = count.get(p, 0) + 1

        return ans