class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(M), len(M[0])
        ans = [[0] * col for r in M];
        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 0;
                for ni in range(i-1, i+2):
                    for nj in range(j-1, j+2):
                        if (ni >= 0 and ni < row and nj >= 0 and nj < col):
                            ans[i][j] += M[ni][nj];
                            count += 1;
                ans[i][j] = ans[i][j]/count;
        return ans;
