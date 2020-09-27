class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = collections.defaultdict(int)
        col = collections.defaultdict(int)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                
        res = 0
        for i in range(m):
            for j in range(n):
                if row[i] == 1 and col[j] == 1 and mat[i][j] == 1:
                    res += 1
        return res
