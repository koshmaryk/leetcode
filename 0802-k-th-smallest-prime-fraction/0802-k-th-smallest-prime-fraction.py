class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        
        hashmap = {}
        fractions = []
        for i in range(n):
            for j in range(n):
                fraction = arr[i] / arr[j]
                fractions.append(fraction)
                hashmap[fraction] = [arr[i], arr[j]]
        
        fractions.sort()
        return hashmap[fractions[k - 1]]
