class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.array = []
        self.size = maxSize
        self.inc = [0] * maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.array) < self.size: self.array.append(x) 
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.array) == 0: return -1
        i = len(self.array) - 1
        inc = self.inc[i]
        if i: self.inc[i - 1] += inc
        self.inc[i] = 0
        return inc + self.array.pop()
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        i = min(k, len(self.array)) - 1
        if i >= 0: self.inc[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
