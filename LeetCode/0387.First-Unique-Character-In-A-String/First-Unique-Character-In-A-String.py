class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
        
