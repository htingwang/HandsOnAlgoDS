class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        s = target.lstrip("0")
        #print(s)
        if not s: return 0
        res = 1
        cur = "1"
        for i in range(1, len(s)):
            if s[i] == cur: continue
            cur = s[i]
            res += 1
        return res
