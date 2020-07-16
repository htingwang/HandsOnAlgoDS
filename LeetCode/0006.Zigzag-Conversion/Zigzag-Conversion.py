class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        res = ""
        n = len(s)
        for i in range(numRows):
            j, k = 0, numRows + numRows - 2
            while j * k + i < n:
                res += s[j * k + i]
                if i != 0 and i != numRows - 1 and j * k + k - i < n:
                    res += s[j * k + k - i]
                j += 1
        return res
                
        
