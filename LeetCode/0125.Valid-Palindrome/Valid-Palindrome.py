class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        if not s: return True;
        left, right = 0, len(s) - 1;
        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdigit():
                left += 1;
            while left < right and not s[right].isalpha() and not s[right].isdigit():
                right -= 1;
            if left < right and s[left].lower() != s[right].lower():
                #print left, right
                return False;
            left += 1;
            right -= 1;
                
        return True;
