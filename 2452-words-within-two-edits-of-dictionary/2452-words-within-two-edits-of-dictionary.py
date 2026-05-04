class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        output = []
        for query in queries:
            for word in dictionary:
                cnt = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        cnt += 1

                if cnt <= 2:
                    output.append(query)
                    break
        return output