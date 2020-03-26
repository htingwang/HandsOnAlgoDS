class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        res = 0
        i = j = 0
        while i < len(target):
            pre = i
            for j in range(len(source)):
                if i < len(target) and source[j] == target[i]:
                    i += 1
            if pre == i:
                return -1
            
            pre = i     
            res += 1
        return res       
