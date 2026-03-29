class Solution:
    '''
    lee(t(c)o)de)

    lee(t(c)o)de
    lee(t(co)de)

    (()))

    c==( stack append
    if stack is empty and c==)
    c==) stack pop


    ((( )

    ''
    ()(())

    ((()))

    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        invalid = set()
        cnt = 0
        for i in range(n):
            if s[i] == "(":
                cnt += 1
            if s[i] == ")":
                if cnt == 0:
                    invalid.add(i)
                    continue
                cnt -= 1

        cnt = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ")":
                cnt += 1
            if s[i] == "(":
                if cnt == 0:
                    invalid.add(i)
                    continue
                cnt -= 1

        sb = []
        for i in range(n):
            if i not in invalid:
                sb.append(s[i])
        return "".join(sb)
