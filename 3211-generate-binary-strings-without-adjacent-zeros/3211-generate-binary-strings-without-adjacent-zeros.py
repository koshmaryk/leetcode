class Solution:
    def validStrings(self, n: int) -> List[str]:
        ss = []
        def gen(prefix):
            if len(prefix) == n:
                ss.append(prefix)
                return
            
            if not prefix or prefix[-1] != "0":
                gen(prefix + "0")
            gen(prefix + "1")

        gen("")
        return ss
