from collections import deque
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
   

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack: m = x
        else: m = max(x, self.stack[-1][1])
        self.stack.append([x, m])
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
 

    def popMax(self):
        """
        :rtype: int
        """
        b = []
        m = self.stack[-1][1]
        while self.stack[-1][0] != m:
            b.append(self.pop())
        m = self.pop()
        map(self.push, reversed(b))
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
