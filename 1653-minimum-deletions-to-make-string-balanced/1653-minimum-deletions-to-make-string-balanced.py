"""

    aababbabb
    aa.abb.bb
        |    

aaabbbb

ans = 2


#b [0:i-1]   
#a [i:n-1]

count_a = 0
ans = 3

count_b = 5




"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        count_b = 0
        for c in s:
            if c == 'b':
                count_b += 1
            elif count_b > 0:
                count_b -= 1
                ans += 1
        return ans