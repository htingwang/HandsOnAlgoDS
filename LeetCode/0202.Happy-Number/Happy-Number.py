class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n
        seen = set([x])
        while True:
            nx = 0
            for c in str(x):
                nx += int(c) ** 2
            if nx == 1: return True
            if nx in seen: return False
            seen.add(nx)
            x = nx
        return True
        
