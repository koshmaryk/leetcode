from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s: str):
            count = 0
            for c in s:
                count += 1 if c == "(" else -1
                if count < 0:
                    return False
            return count == 0

        output = []
        queue = deque([""])
        while queue:
            s = queue.popleft()
            if len(s) == 2 * n:
                if valid(s):
                    output.append(s)
                continue

            queue.append(s + "(")
            queue.append(s + ")")
        return output