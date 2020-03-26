import heapq
from collections import deque

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        minheap = []
        m, n = len(forest), len(forest[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(minheap, (forest[i][j], (i, j)))
        start = (0, 0) 
        #print(minheap)
        while minheap:
            _, cur = heapq.heappop(minheap)
            dist = self.path_distance(forest, start, cur)
            if dist == -1: return -1
            forest[cur[0]][cur[1]] = 1
            res += dist
            start = cur
        return res
    
    def path_distance(self, forest, start, end):
        #print(start, end)
        queue = deque()
        queue.append((start[0], start[1]))
        dist = {(start[0], start[1]): 0}
        while queue:
            i, j = queue.popleft()
            if (i, j) == end: 
                return dist[(i, j)]
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < len(forest) and 0 <= nj < len(forest[0]) and (ni, nj) not in dist and forest[ni][nj] >= 1:
                    dist[(ni, nj)] = dist[(i, j)] + 1
                    queue.append((ni, nj))
        return -1
