class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        # the math property states that every valid () combination can be decomposed to (A)B, 
        # where A and B are also valid () combination (possibly empty)
        #               F(n)
        # ( + F(0) + ) F(n - 1) ... ( + F(n - 1) + ) F(0)
        #
        #                              F(3)
        # ( + F(0) + ) F(2)     ( + F(1) + ) F(1)   ( + F(2) + ) F(0)
        #       ()(())                 (())()           ((()))
        output = []
        for opened in range(n):
            for left_s in self.generateParenthesis(opened):
                for right_s in self.generateParenthesis(n - 1 - opened):
                    output.append("(" + left_s + ")" + right_s)
        return output

        # Time Complexity: 2n! / ((n + 1)! * n!) or 4^n / √n
        # C(n) = C(0) * C(n - 1) + C(1) * C(n - 2) + .. + C(n - 1) * C(0)
        # Space Complexity: 2n