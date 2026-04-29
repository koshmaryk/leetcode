"""



    10,9,2,3,1,5,8

lis = 2 3 

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for num in nums[1::]:
            if num > lis[-1]:
                lis.append(num)
            else:
                i = 0
                while lis[i] < num:
                    i += 1
                lis[i] = num
        return len(lis)
        