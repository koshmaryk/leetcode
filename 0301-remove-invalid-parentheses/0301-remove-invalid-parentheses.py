from collections import deque

'''
()()(() = ()()()
)( = ""
()())() = ()()(), (())()
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        output = set()
        min_removals = float('inf')

        def backtrack(i, opened, closed, expr, removals):
            nonlocal min_removals
            if i == len(s):
                if opened == closed and removals <= min_removals:
                    if removals < min_removals:
                        min_removals = removals
                        output.clear()
                    output.add("".join(expr))
                return

            if s[i] not in "()":
                expr.append(s[i])
                backtrack(i + 1,  opened, closed, expr, removals)
                expr.pop()
            else:
                # exclude curr ( or )
                backtrack(i + 1,  opened, closed, expr, removals + 1)

                # include curr if valid
                expr.append(s[i])
                if s[i] == "(":
                    backtrack(i + 1,  opened + 1, closed, expr, removals)
                if s[i] == ")" and closed < opened:
                    backtrack(i + 1,  opened, closed + 1, expr, removals)
                expr.pop()

        backtrack(0,0,0,[],0)
        return list(output)
        