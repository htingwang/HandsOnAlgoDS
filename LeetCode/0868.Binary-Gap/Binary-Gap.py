class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = N
        anchor = -1
        res = 0
        for i in range(32):
            x = A & 1
            if x == 1:
                if anchor != -1:
                    res = max(res, i - anchor)
                anchor = i
            A >>= 1
        return res
        
