import sys
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if start <= end: res.append([start, end])
            if A[i][1] < B[j][1]: i += 1
            else: j += 1
        return res
