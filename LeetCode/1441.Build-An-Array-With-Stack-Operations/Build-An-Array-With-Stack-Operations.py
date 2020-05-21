class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        j = 0
        for i in range(1, n + 1):
            
            if j > len(target) - 1: 
                break
                
            if target[j] == i:
                res.append("Push")
                j += 1
            else:
                res.extend(["Push", "Pop"])
        return res
