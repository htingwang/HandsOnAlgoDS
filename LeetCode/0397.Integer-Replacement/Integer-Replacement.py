class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.integerReplacement2(n)
    
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        return 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))
    
    def integerReplacement2(self, n):
        res = 0
        while n > 1:
            if n & 1:
                if n & 2 and n != 3: n += 1
                else: n -= 1
            else:
                n /= 2
            res += 1
        return res
