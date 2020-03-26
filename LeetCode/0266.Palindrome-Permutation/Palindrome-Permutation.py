class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd = 0; sdict = {};
        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1;
        for key in sdict:
            if sdict[key] % 2 == 1: odd += 1;
            if odd > 1: return False;
        return True;
