class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bulbSwitch2(n)
    
    def bulbSwitch1(self, n):
        res = 1
        while res ** 2 <= n: res += 1
        return res - 1
    
    def bulbSwitch2(self, n):
        return int(sqrt(n))
