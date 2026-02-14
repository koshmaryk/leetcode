class Solution:
    '''
    [3,3] 6 [0,1]

    [1,2,5,3,8] 4 [0,3]

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        seen = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            
            seen[nums[i]] = i
        return [-1, -1]
        