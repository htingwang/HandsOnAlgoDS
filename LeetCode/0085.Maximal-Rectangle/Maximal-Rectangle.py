class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0;
        def leetcode84(heights):
            ans = 0;
            stack = [];
            for cur in range(len(heights)):
                stack.append(cur);
                while len(stack) > 0 and (cur == len(heights)-1 or heights[cur+1] < heights[stack[-1]]):
                    pop = stack.pop();
                    top = -1;
                    if len(stack) > 0: top = stack[-1];
                    #print [pop, cur, top, stack]
                    ans = max(ans, heights[pop] * (cur-top));
            return ans;
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j]);
                if i > 0:
                    if matrix[i][j] : matrix[i][j] += int(matrix[i-1][j]);
            ans = max(ans, leetcode84(matrix[i]));
        return ans;
            
