class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #k = int(math.sqrt(n))
        prime = [True] * (n)
        res = 0
        for i in range(2, n):
            if prime[i]:
                res += 1
                j = 2
                while i * j < n:
                    prime[i * j] = False
                    j += 1
        return res 
