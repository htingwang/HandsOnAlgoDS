class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            if n % 26 == 0:
                c = 'Z'  
                n -= 26
            else:
                c = chr(ord('A') + n % 26 - 1)
                n -= n % 26
            res = c + res
            n //= 26
            
        return res
