class Solution:
    '''
    bcabc -> abc
    bcac -> bac
    bcdabc -> dabc

    bcabdcd -> abdcd

    

    '''
    from collections import Counter

    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        
        p = 0
        for i in range(len(s)):
            if s[i] < s[p]: p = i

            count[s[i]] -= 1
            if count[s[i]] == 0:
                break

        return s[p] + self.removeDuplicateLetters(s[p::].replace(s[p], "")) if s else ""