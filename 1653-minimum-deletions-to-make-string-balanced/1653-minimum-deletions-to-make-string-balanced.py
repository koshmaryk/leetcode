"""

    aababbabb
    aa.abb.bb
        |    

#b [0:i-1]   
#a [i:n-1]

count_a = 0
ans = 3

count_b = 5




"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        stack = []
        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                stack.pop()
                ans += 1
            else:
                stack.append(c)

        return ans