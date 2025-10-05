class Solution:
    '''
    lee(t(c)o)de)

    stack = (()

    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes = set()
        stack = []
        for i in range(len(s)):
            if s[i] not in '()':
                continue

            if s[i] == '(':
                stack.append(i)
            elif not stack:
                indexes.add(i)
            else:
                stack.pop()

        while stack:
            indexes.add(stack.pop())
                
        ans = []
        for i in range(len(s)):
            if i in indexes:
                continue
            ans.append(s[i])
        return "".join(ans)
        