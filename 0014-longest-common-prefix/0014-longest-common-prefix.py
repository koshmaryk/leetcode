class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] # fl
        for i in range(1, len(strs)): # i = 1 -> flow; i = 2 -> flight 
            j = 0 # [0, 4)
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[0:j]
        return prefix
        