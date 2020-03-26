class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n <= 2: return 1
        T0 = 0
        T1 = T2 = 1
        for i in range(3, n + 1):
            T = T0 + T1 + T2
            T0, T1, T2 = T1, T2, T
        return T
        
