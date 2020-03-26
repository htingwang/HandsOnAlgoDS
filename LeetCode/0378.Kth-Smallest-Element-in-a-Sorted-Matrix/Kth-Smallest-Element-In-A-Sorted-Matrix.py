class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            cnt = self.find_num_by_upperbound(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        #print(left, right)
        return left
    
    def find_num_by_upperbound(self, matrix, upperbound):
        i = 0
        j = len(matrix) - 1
        count = 0
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= upperbound:
                i += 1
                count += j + 1
            else:
                j -= 1
        return count
