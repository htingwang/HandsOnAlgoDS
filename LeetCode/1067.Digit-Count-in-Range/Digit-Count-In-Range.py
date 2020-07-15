class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        return self.digitsCount2(d, low, high)
        
    def digitsCount2(self, d, low, high):
        def count(n):
            res, a = 0, 1
            while a <= n:
                cur = n // a
                prefix = cur // 10 if d else cur // 10 - 1
                if cur % 10 < d: res += prefix * a
                if cur % 10 == d: res += prefix * a + n % a + 1
                if cur % 10 > d: res += (prefix + 1) * a

                a *= 10
            return res
        print(count(high), count(low - 1))
        return count(high) - count(low - 1)
        
        
    def digitsCount1(self, d, low, high):
        def count(n):
            if n < d: return 0
            res = 0
            # if n's unit digit is d
            if d and n % 10 >= d: res += 1
            # number of d in unit digit, 0d, 1d, (n//10-1)d
            res += n // 10
            # number of d in digit greater than unit when n >= n // 10 * 10
            if n // 10: res += str(n // 10).count(str(d)) * (n % 10 + 1)
            # number of d in digit greater than unit when n < n // 10 * 10
            res += count(n // 10 - 1) * 10
            return res

        return count(high) - count(low - 1)
