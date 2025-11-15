class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []

        def generate(opened, closed):
            if opened == n and closed == n:
                output.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                generate(opened + 1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                generate(opened, closed + 1)
                stack.pop()

        generate(0, 0)
        return output