class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)

        total = sum(arr)
        if total % 3 != 0:
            return False

        target_sum = total // 3

        partitions = 0
        curr_sum = 0
        for i in range(n):
            curr_sum += arr[i]
            if curr_sum == target_sum:
                partitions += 1
                curr_sum = 0

                if partitions == 2 and i < n - 1:
                    return True
        return False
