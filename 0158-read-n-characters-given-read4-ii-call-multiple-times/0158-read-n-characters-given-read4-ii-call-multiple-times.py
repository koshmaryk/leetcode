# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.size = 0
        self.ptr = 0

    def read(self, buf: List[str], n: int) -> int:
        read = 0
        while read < n:
            if self.ptr == self.size:
                self.size = read4(self.buf4)
                self.ptr = 0
                if self.size == 0:
                    break

            buf[read] = self.buf4[self.ptr]
            read += 1
            self.ptr += 1

        return read