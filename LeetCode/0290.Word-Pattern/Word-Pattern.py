class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(" ")
        if len(pattern) != len(s): return False
        
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            p, word = pattern[i], s[i]
            if p in m1 and m1[p] != word: return False
            if word in m2 and m2[word] != p: return False
            m1[p], m2[word] = word, p
        return True
