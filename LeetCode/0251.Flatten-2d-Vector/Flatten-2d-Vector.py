class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.stack = []
        for i in range(len(v) - 1, -1, -1):
            self.stack.append(v[i])
        

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        return self.stack.pop()[0]
    
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if len(self.stack[-1]) == 1:
                return True
            cur = self.stack.pop()
            for i in range(len(cur) - 1, -1, -1):
                self.stack.append([cur[i]])
        #if self.stack: return True
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
