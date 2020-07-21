class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 10
        res = 10
        for i in range(2, n + 1):
            cur = 81
            k = 0
            while k < i - 2:
                cur *= (8 - k)
                k += 1
            res += cur
        return res
