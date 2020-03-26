class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2: return True
        mapping = {}
        for c1, c2 in zip(str1, str2):
            if mapping.setdefault(c1, c2) != c2: return False
        return len(set(str2)) < 26
        
