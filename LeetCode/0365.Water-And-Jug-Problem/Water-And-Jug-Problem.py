class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        
        return z == 0 or (x + y >= z and z % gcd(x, y) == 0)
