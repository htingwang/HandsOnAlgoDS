class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0: return 0
        a, b = 0, 1
        for i in range(N - 1):
            a, b = b, a + b      
        return b



        
