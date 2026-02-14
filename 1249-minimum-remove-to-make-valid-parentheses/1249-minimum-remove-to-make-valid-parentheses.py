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
        idx = set()
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue

            if c == '(':
                stack.append(i)
            elif not stack: # )))), )(
                idx.add(i)
            else:  # ()
                stack.pop()

        while stack:
            idx.add(stack.pop())

        output = []
        for i in range(len(s)):
            if i in idx:
                continue
            output.append(s[i])
        return "".join(output)
        