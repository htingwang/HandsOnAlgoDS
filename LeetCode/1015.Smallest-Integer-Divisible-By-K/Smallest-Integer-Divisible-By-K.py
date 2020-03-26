class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0 or K % 5 == 0: return -1;
        r = 0;
        for i in range(1, K + 1):
            r = (10 * r + 1) % K;
            if r == 0: return i;
        return -1;
        
