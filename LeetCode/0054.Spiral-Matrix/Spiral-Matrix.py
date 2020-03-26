class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return [];
        imin, imax, jmin, jmax = 0, len(matrix)-1, 0, len(matrix[0])-1;
        count = i = j = 0;
        di, dj = 0, 1; 
        ans = [];
        while count < len(matrix) * len(matrix[0]):
            #print [i, j, imin, imax, jmin, jmax]
            ans.append(matrix[i][j]);
            if i == imin and j == jmax and [di, dj] == [0, 1]:
                imin += 1;
                di, dj = dj, -di; # 1, 0
            elif i == imax and j == jmax and [di, dj] == [1, 0]:
                jmax -= 1;
                di, dj = dj, -di; # 0, -1
            elif i == imax and j == jmin and [di, dj] == [0, -1]:
                imax -= 1;
                di, dj = dj, -di; # -1, 0
            elif i == imin and j == jmin and [di, dj] == [-1, 0]:
                jmin += 1;
                di, dj = dj, -di; # 0, 1
            #print ["d", di, dj]
            i += di;
            j += dj;
            count += 1;
        return ans;        
                
