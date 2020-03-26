class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < len(t):
            s, t = t, s
        if len(s) - len(t) > 1:
            return False
        
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1 : ] == t[i + 1 : ]
                else:
                    return s[i + 1 :] == t[i : ]
        return len(s) - len(t) == 1
