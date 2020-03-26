import collections
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = abs(x)
        y = abs(y)
        
        if y > x:
            x, y = y, x
            
        if (x, y) == (2, 2):
            return 4
        
        if (x, y) == (1, 0):
            return 3
        
        delta = x - y
        if y <= delta:
            return delta - 2 * ((delta - y) // 4)
        else:
            return delta - 2 * ((delta - y) // 3)
