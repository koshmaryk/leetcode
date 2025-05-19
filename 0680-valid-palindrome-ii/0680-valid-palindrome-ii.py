class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skip = True
                l, r = left + 1, right
                while l < r:
                    if s[l] != s[r]:
                        skip = False
                        break
                    l, r = l + 1, r - 1
                
                if skip:
                    return True

                l, r = left, right - 1
                while l < r:
                    if s[l] != s[r]:
                        return False
                    l, r = l + 1, r - 1

                return True

            left, right = left + 1, right - 1
                
        return True
        