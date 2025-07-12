class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []

        def backtrack(opened, closed):
            if opened == n and closed == n:
                output.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return output

        # Time Complexity: 2n! / ((n + 1)! * n!) or 4^n / √n
        # C(n) = C(0) * C(n - 1) + C(1) * C(n - 2) + .. + C(n - 1) * C(0)
        # Space Complexity: 2n