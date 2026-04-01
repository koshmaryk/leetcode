class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        split = []
        for word in words:
            for s in word.split(separator):
                if s:
                    split.append(s)
        return split
