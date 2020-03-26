class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return -1
        row, col = len(grid), len(grid[0])
        queue = collections.deque()
        res = 0
        fresh = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while queue:
            size = len(queue)
            is_valid = False
            for _ in range(size):
                i, j = queue.popleft()
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))
                        is_valid = True
            if is_valid: 
                #print(i, j)
                res += 1
        #print(fresh)   
        #print(grid)
        return -1 if fresh else res
                    
        
