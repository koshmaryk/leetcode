class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def gen(prefix):
            if len(prefix) == k:
                output.append(prefix[:])
                return

            for c in range(n, 0, -1):
                if len(prefix) > 0 and c >= prefix[-1]:
                    continue

                if c - 1 < k - len(prefix) - 1:
                    break

                prefix.append(c)
                gen(prefix)
                prefix.pop()

        gen([])
        return output