class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, cnt, start = 1, 9, 1
        while n > digit * cnt:
            n -= digit * cnt
            cnt *= 10
            start *= 10
            digit += 1
        start += (n - 1) // digit
        t = str(start)
        return int(t[(n - 1) % digit])
        
