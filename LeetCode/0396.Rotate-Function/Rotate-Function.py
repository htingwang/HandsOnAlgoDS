class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # F(0) = b+2c+3d
        # F(1) = a+2b+3c
        # F(2) = 2a+3b+d
        # F(3) = 3a+c+2d
        # F(1) = F(0) + sum - 4d
        # F(2) = F(1) + sum - 4c
        # F(3) = F(2) + sum - 4b
        # F(i) = F(i - 1) + sum - n * A[n - i]
        n = len(A)
        F = 0
        for i in range(1, n):
            F += i * A[i]
        s = sum(A)
        res = F
        for i in range(1, n):
            F += s - n * A[n - i]
            res = max(res, F)
        return res

