class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans, base = 1, x;
        i = abs(n);
        while i >= 1:     
            if i % 2 == 1:
                ans *= base;
            base *= base;
            if i == -1: break;
            i //= 2;
        if n > 0: return ans;
        return 1/ans;
