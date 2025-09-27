# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque

class Solution:
    '''
    [1,[2,2],[[3],2],1]


    '''
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        ints = [] # int, depth
        max_d, d = 1, 1
        q = deque(nestedList)
        while q:
            max_d = max(max_d, d)
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.isInteger():
                    ints.append((curr.getInteger(), d))
                else:
                    q.extend(curr.getList())
            d += 1

        total = 0
        for integer, d in ints:
            total += integer * (max_d - d + 1)
        return total