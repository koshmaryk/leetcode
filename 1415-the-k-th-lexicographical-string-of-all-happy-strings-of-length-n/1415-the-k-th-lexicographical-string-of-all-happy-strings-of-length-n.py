class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        cnt = k
        ans = ""

        def gen(prefix):
            nonlocal cnt, ans
            if len(prefix) == n:
                cnt -= 1
                if cnt == 0:
                    ans = "".join(prefix)
                return

            for l in "abc":
                if prefix and prefix[-1] == l:
                    continue

                prefix.append(l)
                gen(prefix)
                if ans != "":
                    return
                prefix.pop()

        gen([])
        return ans
