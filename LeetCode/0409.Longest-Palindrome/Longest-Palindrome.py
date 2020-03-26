class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        exists = {};
        ans = 0;
        for i in range(len(s)):
            exists[s[i]] = exists.get(s[i], 0) + 1;
            if exists[s[i]] == 2:
                ans += 2;
                exists[s[i]] = 0;
        #print exists
        for key in exists:
            if exists[key] == 1:
                ans += 1;
                break;
        return ans;
                
                
                
        
