class Solution(object):
    def numDistinctIslands2(self, grid):
        if not grid or not grid[0]: return 0
        queue = collections.deque()
        shapes = set()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0 # visited.add((i, j))
                    shape = []
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        shape.append((cur_i, cur_j))
                        for ni, nj in [(cur_i - 1, cur_j), (cur_i + 1, cur_j), (cur_i, cur_j - 1), (cur_i, cur_j + 1)]:
                            if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                                queue.append((ni, nj))
                                grid[ni][nj] = 0
                    shapes.add(self.canonical(shape))
        return len(shapes)

    def canonical(self, shape):
        res = []
        for i in range(4): # 0, 90. 180, 270 degree
            cur_1 = []
            cur_2 = []
            for x, y in shape:
                cur_1.append(complex(x, y) * (1j ** i)) # (x, yj), (xj, -y), (-x, -yj), (-xj, y)
                cur_2.append(complex(y, x) * (1j ** i)) # (y, xj), (yj, -x), (-y, -xj), (-yj, x)
            w1 = complex(min(z.real for z in cur_1), min(z.imag  for z in cur_1))
            w2 = complex(min(z.real for z in cur_2), min(z.imag  for z in cur_2))
            for j in range(len(cur_1)):
                cur_1[j] = str(cur_1[j] - w1)
            for j in range(len(cur_2)):
                cur_2[j] = str(cur_2[j] - w2)
            res = max(res, sorted(cur_1))
            res = max(res, sorted(cur_2))
            
        return tuple(res)
