class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        sorted_arr = sorted(arr)

        ranks = {}
        rank = 1
        for i in range(n):
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1

            ranks[sorted_arr[i]] = rank

        output = [0] * n
        for i in range(n):
            output[i] = ranks[arr[i]]
        return output
