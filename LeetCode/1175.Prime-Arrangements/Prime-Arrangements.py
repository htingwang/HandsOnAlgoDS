class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        #if n == 2: return 1
        def is_prime(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return 0
            return 1
        
        count = 0
        for i in range(2, n + 1):
            count += is_prime(i)
            
        #print(count)
        return (math.factorial(count) * math.factorial(n - count)) % (pow(10, 9) + 7)
