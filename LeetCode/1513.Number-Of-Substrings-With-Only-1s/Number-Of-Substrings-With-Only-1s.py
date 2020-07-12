class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split('0')
        res = 0
        mod = 10 **9 + 7
        for ones in s:
            l = len(ones)
            res += (l + 1) * l / 2
            res %= mod
        return res
            
        
