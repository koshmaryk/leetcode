"""
minK = 1
maxK = 7

0,1,2,3,4,5,6,7,8
3,1,5,7,2,8,1,4,7


1,5,7
1,5,7,2
1,4,7

1,5,7,2,8,1,4,7
1,5,7,2,8
5,7,2,8
7,2,8
2,8
8
8,1
8,1,4
8,1,4,7


[minK, maxK]
badK...[l..minK...maxK...r]...badK

last_bad < l <= last_minK, last_maxK
last_bad < l <= min(last_minK, last_maxK)

[last_bad + 1, min(last_minK, last_maxK)]

0,1,2,3,4,5,6,7,8,9,10
8,9,1,1,1,1,1,5,7,2,8

min(2, 4) - 1 = 1
min(2, 4) - 1 = 1

1,5,7
1,5,7,2

min(6, 8) - 1 = 5

1,1,1,1,1,5,7,2
1,1,1,1,5,7,2
1,1,1,5,7...
1,1,5,7
1,5,7

"""
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)

        last_bad = last_minK = last_maxK = -1
        cnt = 0
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                last_bad = i

            if nums[i] == minK:
                last_minK = i
            if nums[i] == maxK:
                last_maxK = i

            cnt += max(0, min(last_minK, last_maxK) - last_bad)
        return cnt
        