class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                if c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        output = []
        def gen(prefix):
            if len(prefix) == 2*n:
                if valid(prefix):
                    output.append(prefix)
                return

            gen(prefix + ')')
            gen(prefix + '(')
        
        gen("")
        return output
