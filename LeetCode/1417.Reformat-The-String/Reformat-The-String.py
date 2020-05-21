class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = []
        s2 = []
        for c in s:
            if c.isdigit():
                s1.append(c)
            else:
                s2.append(c)
        if abs(len(s1) - len(s2)) > 1: return ""
        res = []
        if len(s2) > len(s1): s1, s2 = s2, s1
        for i in range(len(s)):
            if i % 2 == 0: res.append(s1[i // 2])
            else: res.append(s2[i // 2])
        
        return "".join(res)
        
        
