class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = set()
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    ans.add(words[i])
                    break
        return list(ans)