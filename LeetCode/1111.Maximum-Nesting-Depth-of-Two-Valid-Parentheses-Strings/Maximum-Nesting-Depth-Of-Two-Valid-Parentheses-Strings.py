class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        left = right = 0
        res = []
        for s in seq:
            if s == "(": 
                left += 1
                if left == right + 1: res.append(0)
                else: res.append(1)
            if s == ")": 
                right += 1
                if left == right: res.append(0)
                else: res.append(1)
        return res
        
