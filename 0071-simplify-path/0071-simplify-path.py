class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split('/'):
            if char == '.' or char == '':
                continue
            
            if char == '..':
                if stack:
                    stack.pop()
                continue
            
            stack.append(char)
        return '/' + '/'.join(stack)
        