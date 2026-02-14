class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []

        def gen(opened, closed):
            if opened == n and closed == n:
                output.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                gen(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                gen(opened, closed + 1)
                stack.pop()

        gen(0, 0)
        return output
