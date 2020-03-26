class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        res = 0
        for p, q in [[1,1],[1,-1],[-1,1],[-1,-1]]:
            closest = arr1[0] * p + arr2[0] * q + 0
            for i in range(len(arr1)):
                cur = arr1[i] * p + arr2[i] * q + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
        return res
        
