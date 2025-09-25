class Solution:
    '''
        "0:start:0","1:start:2","1:end:5","0:end:6"

        "0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"


        2-0=2
        6-5+1=2

        5-2+1=4

        [3,4]

    '''
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n

        s = logs[0].split(":")
        t = int(s[2])
        stack = [s[0]]
        for i in range(1, len(logs)):
            s = logs[i].split(":")
            if s[1] == "start":
                if stack:
                    result[int(stack[-1])] += int(s[2]) - t
                stack.append(s[0])
                t = int(s[2])
            else:
                result[int(stack[-1])] += int(s[2]) - t + 1
                stack.pop()
                t = int(s[2]) + 1
        return result
        