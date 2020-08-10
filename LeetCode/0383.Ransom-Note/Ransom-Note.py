class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = collections.Counter(magazine)
        for c in ransomNote:
            if count[c] == 0: return False
            count[c] -= 1
        return True
