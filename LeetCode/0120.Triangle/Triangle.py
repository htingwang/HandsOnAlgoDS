class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memo = {}
        return self.helper(triangle, 0, 0, memo)
    
    def helper(self, triangle, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(triangle):
            return 0
        
        left = self.helper(triangle, i + 1, j, memo)
        right = self.helper(triangle, i + 1, j + 1, memo)
        memo[(i, j) ] = min(left, right) + triangle[i][j]
        
        return memo[(i, j)]
        
