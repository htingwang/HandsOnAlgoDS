class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and not num & (num - 1) and (num - 1) % 3 == 0
        
