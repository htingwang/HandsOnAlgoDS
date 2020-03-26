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
        left, right = 0, row * col - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            cur = matrix[mid // col][mid % col]
            if cur == target:
                return True
            if cur < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
