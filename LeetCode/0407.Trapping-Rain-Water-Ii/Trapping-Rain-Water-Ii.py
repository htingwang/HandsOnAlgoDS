import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]: return 0
        
        minheap = []
        visited = set()
        
        m, n = len(heightMap), len(heightMap[0])
        
        for i in range(m):
            heapq.heappush(minheap, (heightMap[i][0], i, 0))
            heapq.heappush(minheap, (heightMap[i][n - 1], i, n - 1))
            visited.add((i, 0))
            visited.add((i, n - 1))
            
        for j in range(1, n - 1):
            heapq.heappush(minheap, (heightMap[0][j], 0, j))
            heapq.heappush(minheap, (heightMap[m - 1][j], m - 1, j))
            visited.add((0, j))
            visited.add((m - 1, j))
        
        res = 0
        while minheap:
            h, x, y = heapq.heappop(minheap)
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    res += max(0, h - heightMap[nx][ny])
                    #print(nx, ny, h - heightMap[nx][ny])
                    heapq.heappush(minheap, (max(h, heightMap[nx][ny]), nx, ny))
                    visited.add((nx, ny))
        return res
                    
