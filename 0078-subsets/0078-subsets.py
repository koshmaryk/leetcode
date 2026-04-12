class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def gen(index, prefix):
            output.append(prefix[:])

            for i in range(index, n):
                prefix.append(nums[i])
                gen(i + 1, prefix)
                prefix.pop()
        
        output = []
        gen(0, [])
        return output
        