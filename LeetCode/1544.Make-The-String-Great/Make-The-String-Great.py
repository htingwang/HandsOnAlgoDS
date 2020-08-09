class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        n = len(s)
        i = 0
        while i < len(s) - 1:
            #print(i, s[i], s[i + 1], abs(ord(s[i]) - ord(s[i + 1])))
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                #print(i)
                if i + 2 < len(s):
                    s = s[: i] + s[i + 2:]
                else:
                    s = s[: i]
                #print(s)
                if i > 0:
                    i -= 1
                continue
            i += 1
        return s
