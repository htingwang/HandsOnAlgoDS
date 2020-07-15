class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.countDigitOne2(n)
    
    def countDigitOne2(self, n):
        res, a = 0, 1
        while a <= n:
            cur = n // a
            
            if cur % 10 < 1: res += (cur // 10) * a
            if cur % 10 == 1: res += (cur // 10) * a + n % a + 1
            if cur % 10 > 1: res += (cur // 10 + 1) * a
            a *= 10
        
        return res
    
    def countDigitOne1(self, n):
        if n < 1: return 0
        res = 0
        if n % 10 >= 1: res += 1
        res += n // 10
        if n // 10: res += str(n // 10).count('1') * (n % 10 + 1)
        res += self.countDigitOne1(n // 10 - 1) * 10
        return res
