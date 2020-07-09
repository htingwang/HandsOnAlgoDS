class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.hammingWeight2(n)
    
    def hammingWeight2(self, n):
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
        
    def hammingWeight1(self, n):
        mask = 1
        res = 0
        for i in range(32):
            if n & mask: res += 1
            mask <<= 1
        return res
