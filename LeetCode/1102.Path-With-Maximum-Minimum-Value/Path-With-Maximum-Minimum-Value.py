class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A or not A[0]: return -1
        queue = [(-A[0][0], 0, 0)]
        #visited = set()
        #visited.add((0, 0))
        score = A[0][0]
        A[0][0] = -1
        while queue:
            val, x, y = heapq.heappop(queue)
            score = min(score, -val)
            if x == len(A) - 1 and y == len(A[0]) - 1:
                return score
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(A) and 0 <= ny < len(A[0]) and A[nx][ny] != -1:
                    heapq.heappush(queue, [-A[nx][ny], nx, ny])
                    #visited.add((nx, ny))
                    A[nx][ny] = -1
