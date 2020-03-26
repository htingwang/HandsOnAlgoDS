from collections import deque
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        queue = deque()
        queue.append(tuple(start))
        seen = set()
        seen.add(tuple(start))
        #print(queue, seen)
        while queue:
            i, j = queue.popleft()
            if (i, j) == tuple(destination):
                return True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                while 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] == 0:
                    ni += di
                    nj += dj
                ni -= di
                nj -= dj
                if (ni, nj) not in seen:
                    seen.add((ni, nj))
                    queue.append((ni, nj))
        return False
