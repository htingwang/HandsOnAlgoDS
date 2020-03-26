class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1: return s
        
        s_rev = s[:: -1]
        
        for i in range(n):
            if s[: n - i] == s_rev[i:]:
                return s_rev[: i] + s
            
        return ""
