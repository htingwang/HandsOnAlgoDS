class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for s, e, inc in updates:
            res[s] += inc
            if e + 1 < length: res[e + 1] -= inc
        for i in range(1, length):
            res[i] += res[i - 1]
        return res
        
