class Solution:
    '''
    "2[abc]3[cd]ef"

    stack = []

    Time Complexity: maxK ^ countK * maxEncodedStringLength
    Space Complexity: maxK ^ countK * maxEncodedStringLength
    '''
    def decodeString(self, s: str) -> str:
        stack = []
        curr_s = ""
        curr_k = 0
        for c in s:
            if c.isdigit():
                curr_k = curr_k * 10 + int(c)
            elif c == "[":
                stack.append(curr_s)
                curr_s = ""
                stack.append(curr_k)
                curr_k = 0
            elif c == "]":
                prev_k = stack.pop()
                prev_s = stack.pop()
                curr_s = prev_s + prev_k * curr_s
            else:
                curr_s += c
        return curr_s
