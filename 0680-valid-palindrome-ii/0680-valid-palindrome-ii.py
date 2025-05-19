class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skip1 = True
                l1, r1 = l + 1, r
                while l1 < r1:
                    if s[l1] != s[r1]:
                        skip1 = False
                        break
                    l1 += 1
                    r1 -= 1

                skip2 = True
                l2, r2 = l, r - 1
                while l2 < r2:
                    if s[l2] != s[r2]:
                        skip2 = False
                        break
                    l2 += 1
                    r2 -= 1

                if skip1 or skip2:
                    return True
                else:
                    return False

            l += 1
            r -= 1
                
        return True
        