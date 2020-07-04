import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]: return 0
        minheap = []
        seen = set()
        m, n = len(heightMap), len(heightMap[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(minheap, (heightMap[i][j], i, j)) 
                    seen.add((i, j))
        res = 0
        while minheap:
            h, i, j = heapq.heappop(minheap)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if  0 <= ni < m and 0  <= nj < n and (ni, nj) not in seen:
                    res += max(0, h - heightMap[ni][nj])
                    heapq.heappush(minheap, (max(h, heightMap[ni][nj]), ni, nj))
                    seen.add((ni, nj))
        return res

                    
