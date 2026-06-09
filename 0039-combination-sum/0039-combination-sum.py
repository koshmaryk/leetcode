class Solution:
    '''
    TC O(n^ T/m)
    SC O(T/m)
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        output = []

        def gen(curr_sum, start, prefix):
            if curr_sum > 0:
                for i in range(start, n):
                    prefix.append(candidates[i])
                    gen(curr_sum - candidates[i], i, prefix)
                    prefix.pop()
            elif curr_sum < 0:
                return
            else:
                output.append(prefix[:])
                return

        gen(target, 0, [])
        return output