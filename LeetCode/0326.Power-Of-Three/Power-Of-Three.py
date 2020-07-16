class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3^19 = 1162261467
        return n > 0 and 1162261467 % n == 0
        
