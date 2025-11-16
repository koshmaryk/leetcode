class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ((((((((((((
        def valid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                if c == ")":
                    count -=1
                if count < 0:
                    return False
            return count == 0

        output = []

        def dfs(s):
            if len(s) == 2 * n:
                if valid(s):
                    output.append(s)
                return

            dfs(s + "(")
            dfs(s + ")")

        dfs("")
        return output