class Solution:
    '''
    n = 10

    0 1 2 3 4 5 6 7 8 9
    0 0 1 1 0 1 0 1 0 0


    '''
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        nums = [1] * n
        nums[0] = 0
        nums[1] = 0

        for num in range(2, int(n**0.5) + 1):
            if nums[num] == 1:
                for multiple in range(num * num, n, num):
                    nums[multiple] = 0
        return sum(nums)