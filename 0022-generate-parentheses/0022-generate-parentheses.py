class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s: str):
            count = 0
            for c in s:
                count += 1 if c == "(" else -1
                if count < 0:
                    return False
            return count == 0

        def dfs(s: str):
            if len(s) == 2 * n:
                if valid(s):
                    output.append(s)
                return

            dfs(s + "(")
            dfs(s + ")")


        output = []
        dfs("")
        return output