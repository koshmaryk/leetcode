class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPalindromeHelper(l: int, r: int, i: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    if i > 0:
                        return validPalindromeHelper(l + 1, r, 0) or validPalindromeHelper(l, r - 1, 0)
                    else:
                        return False
                l += 1
                r -= 1
                
            return True

        return validPalindromeHelper(0, len(s) - 1, 1)
        