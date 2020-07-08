class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count how many 5n, 25n, 125n....
        res = 0
        while n:
            n //= 5
            res += n
        return res
