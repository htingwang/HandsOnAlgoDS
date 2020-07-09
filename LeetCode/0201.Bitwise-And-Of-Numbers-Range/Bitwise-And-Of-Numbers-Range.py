class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.rangeBitwiseAnd2(m, n)
    
    def rangeBitwiseAnd2(self, m, n):
        while m < n:
            n = n & (n - 1)
        return m & n
        
    def rangeBitwiseAnd1(self, m, n):
        shift = 0
        while m < n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift
