class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        res = []
        
        while i >= 0 or j >= 0:
            s1 = int(a[i]) if i >= 0 else 0
            s2 = int(b[j]) if j >= 0 else 0
            #print(s1, s2)
            s = s1 + s2 + carry
            carry = s >> 1
            res.append(str(s % 2))
            
            i -= 1
            j -= 1
        if carry:
            res.append("1")
            
        return "".join(res[::-1])
