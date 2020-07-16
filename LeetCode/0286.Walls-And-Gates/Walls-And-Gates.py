class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return
        mx = 2147483647
        queue = collections.deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: queue.append((0, i, j))
                    
        while queue:
            d, i, j = queue.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == mx:
                    rooms[ni][nj] = d + 1
                    queue.append((d + 1, ni, nj))
        
