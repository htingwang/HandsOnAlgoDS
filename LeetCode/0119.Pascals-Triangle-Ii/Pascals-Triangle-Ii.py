class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1];
        
        ans = [1] * (rowIndex+1);
        
        dividend, dividor = 1, 1;
        for i in range(1, rowIndex/2 + 1):
            dividend *= (rowIndex - i + 1);
            dividor *= i;
            ans[i] = dividend/dividor;
            
        for i in range(rowIndex/2 + 1, rowIndex + 1):
            ans[i] = ans[rowIndex - i];
            
        return ans;
            
