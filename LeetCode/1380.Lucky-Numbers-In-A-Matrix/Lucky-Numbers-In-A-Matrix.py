class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m, n = len(matrix), len(matrix[0])
        a = set()
        for i in range(m):
            tmp = float('inf')
            for j in range(n):
                tmp = min(tmp, matrix[i][j])
            a.add(tmp)
        for j in range(n):
            tmp = float('-inf')
            for i in range(m):
                tmp = max(tmp, matrix[i][j])
            if tmp in a: res.append(tmp)
        return res
