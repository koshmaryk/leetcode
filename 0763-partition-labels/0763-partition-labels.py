"""
012345
ababcc

s = -1
e = max(e, last_occurrence[ord(c) - ord('a')])

e - s

answer = [4, 2]

a 2
b 3
c 5


"""
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = [0] * 26
        for i, c in enumerate(s):
            last_occurrence[ord(c) - ord('a')] = i

        answer = []
        start, end = -1, 0
        for i, c in enumerate(s):
            end = max(end, last_occurrence[ord(c) - ord('a')])
            if i == end:
                answer.append(end - start)
                start = end
        return answer
        