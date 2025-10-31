class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurence = {c:i for i,c in enumerate(s)}

        seen = set()
        stack = []
        for i,c in enumerate(s):
            if c not in seen:
                while stack and stack[-1] > c and last_occurence[stack[-1]] > i:
                    seen.remove(stack.pop())

                seen.add(c)
                stack.append(c)
        return ''.join(stack)
