from collections import deque
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        res = 0
        queue = deque()
        queue.append(start)
        dist = {(start[0], start[1]): 0}
        while queue:
            i, j = queue.popleft()
            #if [i, j] == destination:
            #    return dist[(i, j)]
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                while 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] == 0:
                    ni += di
                    nj += dj
                ni -= di
                nj -= dj
                #print(i, j, ni, nj)
                steps = dist[(i, j)] + abs(i - ni) + abs(j - nj)
                if ((ni, nj) not in dist or steps < dist[(ni, nj)]) and (ni, nj) != (i, j):
                    dist[(ni, nj)] = steps
                    queue.append((ni, nj))
        #print(dist)
        if (destination[0], destination[1]) in dist: return dist[(destination[0], destination[1])]
        return -1
