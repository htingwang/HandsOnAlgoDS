class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for j in range(len(matrix[0])-1):
            for i in range(len(matrix)-1):
                if matrix[i][j] != matrix[i+1][j+1] :
                    return False;
        return True;
            
        
