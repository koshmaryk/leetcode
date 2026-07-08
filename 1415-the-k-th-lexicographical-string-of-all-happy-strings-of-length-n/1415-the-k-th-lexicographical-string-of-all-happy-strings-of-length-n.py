class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        cnt = k

        def gen(prefix):
            nonlocal cnt
            if len(prefix) == n:
                cnt -= 1
                if cnt == 0:
                    return "".join(prefix)
                return ""

            for l in letters:
                if prefix and prefix[-1] == l:
                    continue

                prefix.append(l)
                s = gen(prefix)
                if s:
                    return s
                prefix.pop()
            return ""

        return gen([])
