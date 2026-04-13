class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        output = []
        def gen(index, prefix):
            output.append(prefix[:])

            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                prefix.append(nums[i])
                gen(i + 1, prefix)
                prefix.pop()

        gen(0, [])
        return output

"""
0,1,2
1,2,2
        0,1
proceed 1,2
     0,2
skip 1,2



"""