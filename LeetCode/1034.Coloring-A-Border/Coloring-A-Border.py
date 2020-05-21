class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        stack = [(r0, c0)]
        seen = set(stack)
        while stack:
            r, c = stack.pop()
            cnt = 0
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < m and 0 <= nc < n:
                    if abs(grid[nr][nc]) == abs(grid[r][c]):
                        cnt += 1
                        if (nr, nc) not in seen: 
                            stack.append((nr, nc))
                            seen.add((nr, nc))
                #else:
                #    cnt += 1
            print(r, c, cnt)
            if cnt < 4:
                grid[r][c] *= (-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0: grid[i][j] = color
        return grid
                    
        
