class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numSquares2(n) 
    
    def numSquares2(self, n):   
        while n % 4 == 0: n /= 4
        if n % 8 == 7: return 4
        i = 0
        while i ** 2 <= n:
            j = int(sqrt(n - i ** 2))
            if i ** 2 + j ** 2 == n:
                if not i: return 1
                return 2
            i += 1
        return 3
        
    def numSquares1(self, n):    
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n + 1):
            j = 1
            while i + j ** 2 <= n:
                dp[i + j ** 2] = min(dp[i + j ** 2], dp[i] + 1)
                j += 1

        return dp[n]
