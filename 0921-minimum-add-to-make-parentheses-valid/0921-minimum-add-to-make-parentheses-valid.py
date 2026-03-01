"""

))((
4

(()()))


())

()))((

"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        min_to_add = 0
        open_brackets = 0
        for c in s:
            if c == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_to_add += 1
        return open_brackets + min_to_add
            