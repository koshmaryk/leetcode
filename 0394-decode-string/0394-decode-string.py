class Solution:
    '''
    "2[abc]3[cd]ef"

    stack = abcabc 3

    abcabccdcdcdef
    
    curr_s = abcabccdcdcdef
    curr_k = 0

    Time Complexity: maxK ^ countK * maxEncodedStringLength
    Space Complexity: maxK ^ countK * maxEncodedStringLength
    '''
    def decodeString(self, s: str) -> str:
        curr_s = ""
        curr_k = 0
        stack = []
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