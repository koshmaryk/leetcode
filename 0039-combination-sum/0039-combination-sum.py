class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        output = []

        def gen(remainder, start, prefix):
            if remainder > 0:
                for i in range(start, n):
                    prefix.append(candidates[i])
                    gen(remainder - candidates[i], i, prefix)
                    prefix.pop()
            elif remainder < 0:
                return
            else:
                output.append(prefix[:])
                return

        gen(target, 0, [])
        return output