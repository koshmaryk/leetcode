class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for c in path.split("/"):
            if c == "." or c == "":
                continue

            if c == "..":
                if stack:
                    stack.pop()
                continue

            stack.append(c)

        return "/" + "/".join(stack)