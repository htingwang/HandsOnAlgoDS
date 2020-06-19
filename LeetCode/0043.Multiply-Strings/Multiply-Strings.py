class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = []
        vals = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p1, p2 = i + j, i + j + 1
                s = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + vals[p2]
                vals[p1] += s // 10
                vals[p2] = s % 10
                
        for val in vals:
            if res or val != 0: res.append(chr(val + ord('0')))
                
        return "".join(res) if res else "0"
