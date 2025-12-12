class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = set()
        answer = []

        def gen(prefix):
            if len(prefix) == n:
                answer.append(prefix[:])
                return
            
            for i in range(n):
                if nums[i] not in used:
                    used.add(nums[i])
                    prefix.append(nums[i])
                    gen(prefix)
                    prefix.pop()
                    used.remove(nums[i])

        gen([])
        return answer
