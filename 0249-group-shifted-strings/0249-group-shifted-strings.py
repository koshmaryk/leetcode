from collections import defaultdict

class Solution:
    '''
    a, z, 
    az, ba, be
    abc, bcd
    abcd


    97 122 = 25
    98 97 = 1
    '''
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def shift_char(c: str, shift: int):
            return chr((ord(c) - shift) % 26 + ord('a'))

        def get_hash(s: str):
            shift = ord(s[0])
            return ''.join(shift_char(c, shift) for c in s)

        groups = defaultdict(list)
        for s in strings:
            key = get_hash(s)
            groups[key].append(s)
        return list(groups.values())
        