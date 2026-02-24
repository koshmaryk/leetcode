class Solution:
    '''
    word=sub stitu tion

    abbr=sub 5 u 4



    '''
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p = q = 0
        while p < len(word) and q < len(abbr):
            if abbr[q].isdigit():
                if abbr[q] == "0":
                    return False

                shift = 0
                while q < len(abbr) and abbr[q].isdigit():
                    shift = shift * 10 + int(abbr[q])
                    q += 1
                p += shift
            else:
                if word[p] != abbr[q]:
                    return False

                p += 1
                q += 1
        return p == len(word) and q == len(abbr)