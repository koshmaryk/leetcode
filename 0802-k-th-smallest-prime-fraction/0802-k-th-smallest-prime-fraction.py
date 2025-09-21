class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        
        fractions = []
        for i in range(n):
            for j in range(n):
                fractions.append((arr[i] / arr[j], arr[i], arr[j]))
        
        fractions.sort()
        f, p, q = fractions[k - 1]
        return [p, q]
