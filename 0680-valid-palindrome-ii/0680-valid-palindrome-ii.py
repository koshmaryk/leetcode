class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                right = True
                l1, r1 = l + 1, r
                while l1 < r1:
                    if s[l1] != s[r1]:
                        right = False
                        break
                    l1 += 1
                    r1 -= 1

                left = True
                l2, r2 = l, r - 1
                while l2 < r2:
                    if s[l2] != s[r2]:
                        left = False
                        break
                    l2 += 1
                    r2 -= 1

                if left or right:
                    return True
                else:
                    return False

            l += 1
            r -= 1
                
        return True
        