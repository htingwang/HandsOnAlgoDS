class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s2t = {}
        t2s = {}
        
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            s2t[s[i]] = t[i]
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            t2s[t[i]] = s[i]
        return True
        
