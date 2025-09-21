class Solution:
    '''

    1,2,3,5


    '''
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        def count(f):
            max_f = 0.0
            args = []
            cnt = 0
            for i in range(n):
                j = 1
                while j < n and arr[i] >= f * arr[j]:
                    j += 1

                cnt += n - j

                if j < n and max_f < arr[i] / arr[j]:
                    max_f = arr[i] / arr[j]
                    args = [arr[i], arr[j]]
            return cnt, args

        answer = []

        bad, good = 0.0, 1.0
        while good - bad > 0.000000001:
            guess = (bad + good) / 2
            cnt, answer = count(guess)
            if cnt > k:
                good = guess
            elif cnt < k:
                bad = guess
            else:
                return answer
        return answer