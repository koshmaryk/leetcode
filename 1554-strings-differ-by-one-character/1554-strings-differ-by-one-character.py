class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        MOD = 10**11 + 7
        n, m = len(dict), len(dict[0])

        hashes = [0] * n
        for i in range(n):
            for c in dict[i]:
                hashes[i] = (26 * hashes[i] + (ord(c) - ord('a'))) % MOD

        
        base = 1
        for j in range(m - 1, -1, -1):
            seen = set()
            for i in range(n):
                h = (hashes[i] - base * (ord(dict[i][j]) - ord('a'))) % MOD
                if h in seen:
                    return True
                seen.add(h)

            base = 26 * base % MOD
        return False