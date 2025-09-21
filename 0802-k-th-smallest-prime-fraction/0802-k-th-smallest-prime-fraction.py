class Solution:
    '''

    1,2,3,5

    0,5 0,33, 0,2

    1/2 1/3


    '''
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        def count(f):
            args = []
            max_f = 0.0
            cnt = 0
            for i in range(n):
                j = 1
                while j < n and arr[i] / arr[j] >= f:
                    j += 1

                cnt += n - j

                if j < n and max_f < arr[i] / arr[j]:
                    max_f = arr[i] / arr[j]
                    args = [arr[i], arr[j]]
            return cnt, args

        answer = []
        bad, good = 0.0, 1.0
        for _ in range(100):
            guess = (bad + good) / 2
            cnt, answer = count(guess)
            if cnt > k:
                good = guess
            elif cnt < k:
                bad = guess
            else:
                return answer
        return answer
