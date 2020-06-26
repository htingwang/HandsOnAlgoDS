class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num, dot, e, num_after_e = False, False, False, True
        s = s.strip(" ")

        for i, c in enumerate(s):
            if c.isdigit():
                num = True
                if e: num_after_e = True
            elif c == '.':
                if dot or e: return False
                dot = True
            elif c == 'e':
                if not num or e: return False
                num_after_e = False
                e = True
            elif c == '+' or c == '-':
                if not (i == 0 or s[i - 1] == 'e'): return False
            else: return False
                
        return num and num_after_e
        
