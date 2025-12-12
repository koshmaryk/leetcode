class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = set()
        answer = []

        def gen(prefix):
            if len(prefix) == n:
                answer.append(prefix)
                return
            
            for i in range(n):
                if nums[i] not in used:
                    used.add(nums[i])
                    gen(prefix + [nums[i]])
                    used.remove(nums[i])

        gen([])
        return answer
