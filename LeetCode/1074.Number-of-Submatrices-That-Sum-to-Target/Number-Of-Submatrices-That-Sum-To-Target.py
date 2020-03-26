from collections import defaultdict
class Solution(object):
    def numSubmatrixSumTarget(self, A, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(A), len(A[0])
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in range(m):
            tmp = [0] * n
            for j in range(i, m):
                c = defaultdict(int)
                c[target] = 1
                for k in range(n):
                    tmp[k] += A[j][k]
                    res += c[tmp[k]]
                    c[tmp[k] + target] += 1
        return res   
