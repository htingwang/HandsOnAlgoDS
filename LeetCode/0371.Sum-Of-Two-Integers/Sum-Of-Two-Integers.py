class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        if b == 0: 
            return a if a < 0x7fffffff else ~(a ^ 0xffffffff)
        s = (a ^ b) & 0xffffffff
        c = ((a & b) << 1) & 0xffffffff

        return self.getSum(s, c)
