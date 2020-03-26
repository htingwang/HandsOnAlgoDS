class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxarea = 0;
        seen = set();
        def dfs(r, c):
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] and (r,c) not in seen:
                seen.add((r,c));
                return 1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1);
            return 0;
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxarea = max(maxarea, dfs(r,c));
        return maxarea;
