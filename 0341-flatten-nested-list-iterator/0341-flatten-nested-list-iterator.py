# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

"""
[1,[2,[3]],4]

D <= L


[2,[3]] = 0
[1,[2,[3]],4] = 0

next 1, next 2, next 3, next 4

"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [(nestedList, 0)]
        
    
    def next(self) -> int:
      self._flatten_list()
      nested, index = self.stack[-1]
      self.stack[-1] = (nested, index + 1)
      return nested[index].getInteger()


    def hasNext(self) -> bool:
        self._flatten_list()
        return len(self.stack) > 0


    def _flatten_list(self):
        while self.stack:
            nested, index  = self.stack[-1]

            if len(nested) == index:
                self.stack.pop()
                continue

            if nested[index].isInteger():
                break
           
            self.stack[-1] = (nested, index + 1)
            self.stack.append((nested[index].getList(), 0))

            

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())