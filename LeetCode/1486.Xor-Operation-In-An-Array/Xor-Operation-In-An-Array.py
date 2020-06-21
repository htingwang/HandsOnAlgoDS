class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = 0
        for _ in range(n):
            res = res ^ start
            start += 2
        return res
        
