from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        answer = []

        def gen(prefix, counter):
            if len(prefix) == n:
                answer.append(prefix[:])
                return

            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    prefix.append(num)
                    gen(prefix, counter)
                    prefix.pop()
                    counter[num] += 1

        gen([], counter)
        return answer