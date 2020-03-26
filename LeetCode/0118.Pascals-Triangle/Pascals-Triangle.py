class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return [];
        ans = [[1]];
        for i in range(1, numRows):
            row = [];
            row.append(1);
            for j in range(1, i):
                row.append(ans[i-1][j-1]+ans[i-1][j]);
            row.append(1);
            ans.append(row);
        return ans;
            
        
