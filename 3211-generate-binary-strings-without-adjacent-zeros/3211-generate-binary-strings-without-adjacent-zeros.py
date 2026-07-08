class Solution:
    def validStrings(self, n: int) -> List[str]:
        ss = []
        def gen(prefix):
            if len(prefix) == n:
                ss.append("".join(prefix))
                return
            
            prefix.append("1")
            gen(prefix)
            prefix.pop()
            
            if not prefix or prefix[-1] != "0":
                prefix.append("0")
                gen(prefix)
                prefix.pop()

        gen([])
        return ss
