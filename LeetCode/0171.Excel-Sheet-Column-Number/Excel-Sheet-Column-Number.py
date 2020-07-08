class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            res += (26 ** i) * (ord(s[n - 1 - i]) - ord('A') + 1)
        return res
        
