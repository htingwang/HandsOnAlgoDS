class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        
        def dfs(grid, i, j, visited, memo, steps):
            
            #print i, j
            #if i==2 and j==2: print visited
            if 0 <= i < N and 0 <= j < N:
  
                if visited[i][j] == 1: return -1
                if i == N - 1 and j == N - 1:
                    return 1
                if grid[i][j] == 1: return -1
                
                
                if (i, j) in memo: 
                    if steps >= memo[(i, j)]: return -1
                else:
                    memo[(i, j)] = steps
                    
                print i, j, steps
                if (i, j) in memo: print memo[(i, j)]                
    
                ans = sys.maxint

                for delta_i, delta_j in [(-1,-1),(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    visited[i][j] = 1
                    subans = dfs(grid, i + delta_i, j + delta_j, visited, memo, steps + 1)
                    visited[i][j] = 0
                    if subans != -1:
                        #if i == 2 and j == 2: print subans, memo
                        ans = min(ans, subans + 1)
                
                if ans == sys.maxint: return -1

                return ans
            return -1
        #ans = sys.maxint
        visited = [[0] * N for _ in range(N)]
        memo = {}
        steps = 1
        #ans = dfs(grid, 0, 0, visited, memo, steps)

        queue = collections.deque([(0, 0)])
        ans = 0
        distance = {(0, 0): 1}
        while queue:
            i, j = queue.popleft()
            for delta_i, delta_j in [(-1,-1),(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                next_i = i + delta_i
                next_j = j + delta_j
                if 0 <= next_i < N and 0 <= next_j < N and grid[next_i][next_j] == 0 and (next_i, next_j) not in distance:
                        queue.append((next_i, next_j))
                        distance[(next_i, next_j)] = distance[(i, j)] + 1
                    
                        if next_i == N - 1 and next_j == N - 1:
                            return distance[(next_i, next_j)]

                                            
        return -1
                                            
        if ans == sys.maxint: return -1
        return ans
        
        
