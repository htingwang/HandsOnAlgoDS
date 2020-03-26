class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "": return 0
        #print str
        ans = 0
        sign = 1
        sign_cnt = 0
        i = 0
        if str[0] == "+":
            i = 1
        if str[0] == "-":
            sign = -1 
            i = 1
        
        for i in range(i, len(str)):
            num = (ord(str[i]) - ord("0"))
            if 0 <= num <= 9:
                ans = ans * 10 + num
            else:
                break
        #print sign, num
        if sign == -1: return max(-ans, pow(-2, 31))       
        return min(ans, pow(2, 31) - 1)
        
