class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        c = 0
        i, j = len(num1) - 1, len(num2) - 1
        res = ""
        while i >= 0 or j >= 0:
            s1 = s2 = 0
            if i >= 0: s1 = int(num1[i])
            if j >= 0: s2 = int(num2[j])
            s = s1 + s2 + c
            res += str(s % 10)
            c = s // 10
            i -= 1
            j -= 1
            
        if c: res += "1"
        return res[ :: -1]
            
        
