class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        
        queue = collections.deque()
        res = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    queue.append((i, j))
                    grid[i][j] = "0"
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        #print(cur_i, cur_j)
                        for ni, nj in [(cur_i + 1, cur_j), (cur_i - 1, cur_j), (cur_i, cur_j + 1), (cur_i, cur_j - 1)]:
                            if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == "1":
                                queue.append((ni ,nj))
                                grid[ni][nj] = "0"
                                
                    res += 1
        return res
