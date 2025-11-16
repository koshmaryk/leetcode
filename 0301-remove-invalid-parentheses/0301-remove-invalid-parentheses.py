class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answer = set()
        longest = float('-inf')

        def dfs(idx, opened, closed, expr):
            nonlocal longest
            if idx == len(s):
                if opened == closed:
                    if len(expr) > longest:
                        longest = len(expr)
                        answer.clear()
                        answer.add("".join(expr))

                    if len(expr) == longest:
                        answer.add("".join(expr))
                return

            char = s[idx]
            if char == "(":
                dfs(idx + 1, opened, closed, expr)

                expr.append(char)    
                dfs(idx + 1, opened + 1, closed, expr)
                expr.pop()

            elif char == ")":
                dfs(idx + 1, opened, closed, expr)

                if closed < opened:
                    expr.append(char)    
                    dfs(idx + 1, opened, closed + 1, expr)
                    expr.pop()
            else:
                expr.append(char)    
                dfs(idx + 1, opened, closed, expr)
                expr.pop()
        
        dfs(0, 0, 0, [])
        return list(answer)