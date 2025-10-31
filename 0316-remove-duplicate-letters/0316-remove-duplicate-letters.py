class Solution:
    '''
    bcabc -> abc
    bcac -> bac
    bcdabc -> dabc

    bcabdcd -> abdcd

    bcab -> bca

    '''
    from collections import Counter

    def removeDuplicateLetters(self, s: str) -> str:
        last_occurence = {c:i for i, c in enumerate(s)}

        seen = set()
        stack = []
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurence[stack[-1]]:
                    seen.remove(stack.pop())

                seen.add(c)
                stack.append(c)
        return "".join(stack)