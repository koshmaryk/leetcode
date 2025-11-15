from collections import deque

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
        queue = deque([s])
        while queue and not output:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if valid(curr):
                    output.add(curr)

                for i in range(len(curr)):
                    candidate = curr[:i] + curr[i+1:]
                    if candidate not in visited and curr[i] in "()":
                        visited.add(candidate)
                        queue.append(candidate)

        return list(output)
        