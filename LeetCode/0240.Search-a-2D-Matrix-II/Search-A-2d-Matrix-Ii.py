class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while 0 <= i < row and 0 <= j < col:
            if matrix[i][j] == target:
                i += 1
                j -= 1
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
