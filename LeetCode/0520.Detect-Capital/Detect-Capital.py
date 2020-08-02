class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word: return True
        if len(word) == 1: return True
        if ord("A") <= ord(word[0]) <= ord("Z"): first = True
        else: first = False
        
        second = True
        if len(word) > 1 and "a" <= word[1] <= "z": second = False
            
        #if len(word) == 2: return first or not second
        
        for i in range(2, len(word)):
            if "a" <= word[i] <= "z" and second: return False
            if "A" <= word[i] <= "Z" and not second: return False
        return first or not second
        
