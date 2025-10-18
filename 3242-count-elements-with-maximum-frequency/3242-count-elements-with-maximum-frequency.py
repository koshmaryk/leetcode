class Solution:
    '''
    [1,2,2,3,4,1]

    [0,2,2,1,1,0]

    [0,0,1,1,2,2]
    '''
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = [0] * 101
        for num in nums:
            count[num] += 1

        count.sort()

        ans = 0
        max_cnt = count[100]
        for i in range(100, -1, -1):
            if count[i] == max_cnt:
                ans += max_cnt
        return ans
        