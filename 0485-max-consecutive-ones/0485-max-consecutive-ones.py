"""
[1,0,1,1,0,1]

cnt=1
ans=2 

"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans
        