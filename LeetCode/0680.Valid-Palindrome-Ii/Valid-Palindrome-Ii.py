class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        if not s: return True;
        left, right = 0, len(s) - 1;
        while left < right:
            if s[left] != s[right]:
                return False;
            left += 1;
            right -= 1;    
        return True;
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True;
        left, right = 0, len(s) - 1;
        while left < right:
            if s[left] != s[right]: 
                return self.isPalindrome(s[left+1 : right+1]) or self.isPalindrome(s[left : right])
            left += 1;
            right -= 1;
         
        return True;
        
