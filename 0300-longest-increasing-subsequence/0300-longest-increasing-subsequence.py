"""



    10,9,2,3,1,5,8

lis =

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for num in nums[1::]:
            i = bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else:
                lis[i] = num
        return len(lis)
        