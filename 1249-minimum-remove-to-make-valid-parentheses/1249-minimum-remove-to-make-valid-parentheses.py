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
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        
        def remove_invalid(string, opened, closed):
            sb = []
            cnt = 0
            for c in string:
                if c == opened:
                    cnt += 1
                if c == closed:
                    if cnt == 0:
                        continue
                    cnt -= 1
                sb.append(c)
            return "".join(sb)

        s = remove_invalid(s, "(", ")")
        s = remove_invalid(s[::-1], ")", "(")
        return s[::-1]
        