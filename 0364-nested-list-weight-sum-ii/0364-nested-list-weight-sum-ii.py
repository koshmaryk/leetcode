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

    integer * (max_d - d + 1)
    
    '''
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nestedList, d):
            max_d = 1
            s, p = 0, 0
            for nested in nestedList:
                if nested.isInteger():
                    s += nested.getInteger()
                    p += nested.getInteger() * d
                    max_d = max(max_d, d)
                else:
                    maxq, sq, pq = dfs(nested.getList(), d + 1)
                    s += sq
                    p += pq
                    max_d = max(max_d, maxq)
            return max_d, s, p


        max_d, s, p = dfs(nestedList, 1)
        return max_d * s - p + s
       