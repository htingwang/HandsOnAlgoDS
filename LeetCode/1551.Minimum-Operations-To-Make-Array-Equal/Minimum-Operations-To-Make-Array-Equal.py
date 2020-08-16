class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # [1,3,5,7,9,11], 5 + 3 + 1
        # [1,3,5,7,9], 4 + 2
        # (a + ( a + (n - 1)d) ) * n / 2
        
        if n % 2 == 0:
            return (1 + 1 + (n // 2 - 1) * 2) * (n // 2) / 2
        else:
            return (2 + 2 + (n // 2 - 1) * 2) * (n // 2) / 2
        
