# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        #print(list(nestedList))
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])
            #print(nestedList[i])
        #print(self.stack[0])

    def next(self):
        """
        :rtype: int
        """
        #print("next")
        #print(self.stack)
        
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            cur = self.stack.pop()
            
            if not cur.isInteger():
                cur = cur.getList()
                #print(type(cur))

                for i in range(len(cur) - 1, -1, -1):
                    self.stack.append(cur[i])
            #else: return cur
            else: 
                self.stack.append(cur)
                return True
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
