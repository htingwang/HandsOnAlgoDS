class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.isPowerOfTwo3(n)
    
    def isPowerOfTwo3(self, n):
        if n == 0: return False
        return n & (n - 1) == 0
    
    def isPowerOfTwo2(self, n):
        if n == 0: return False
        return n & (-n) == n
    
    def isPowerOfTwo1(self, n):
        while n:
            if n & 1 == 1: break
            n >>= 1
        return n == 1
