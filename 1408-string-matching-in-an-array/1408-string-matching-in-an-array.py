class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        n = len(words)
        ans = set()
        for i in range(n):
            parts = []
            for j in range(i + 1, n):
                parts.append(words[j])

            if words[i] in "#".join(parts):
                ans.add(words[i])
        return list(ans)