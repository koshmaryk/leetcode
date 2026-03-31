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
        invalid = set()
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    invalid.add(i)

        while stack:
            invalid.add(stack.pop())

        sb = []
        for i, c in enumerate(s):
            if i not in invalid:
                sb.append(c)
        return "".join(sb)
