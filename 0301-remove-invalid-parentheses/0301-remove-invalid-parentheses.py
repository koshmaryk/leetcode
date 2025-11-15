from collections import deque

'''
()()(() = ()()()
)( = ""
()())() = ()()(), (())()
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(candidate):
            count = 0
            for c in candidate:
                if c == "(":
                    count += 1
                if c == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        output = set()
        visited = set()

        min_depth = float('inf')

        def dfs(curr, depth):
            nonlocal min_depth
            if valid(curr): # O(n)
                if depth == min_depth:
                    output.add(curr)
                if depth < min_depth:
                    min_depth = depth
                    output.clear()
                    output.add(curr)
                return

            for i in range(len(curr)):
                candidate = curr[:i] + curr[i+1:]
                if candidate not in visited and curr[i] in "()":
                    visited.add(candidate)
                    dfs(candidate, depth + 1)

        dfs(s, 0)

        return list(output)
        