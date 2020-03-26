class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cnt = 0
        for c in s:
            if c == "R":
                cnt += 1
            if c == "L":
                cnt -= 1
            if cnt == 0:
                res += 1
        return res
            
        
