class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        G = [[[], []] for _ in range(n)]
        for i, j in red_edges: G[i][0].append(j)
        for i, j in blue_edges: G[i][1].append(j)
        sols = [[sys.maxsize, sys.maxsize] for _ in range(n)]
        sols[0] = [0, 0]
        queue = collections.deque([[0, 0], [0, 1]])
        while queue:
            node, color = queue.popleft()
            for next_node in G[node][color]:
                if sols[next_node][color] == sys.maxsize:
                    sols[next_node][color] = sols[node][1 - color] + 1
                    queue.append([next_node, 1 - color])
        res = []
        for sol in sols:
            cur = min(sol)
            if cur == sys.maxsize: res.append(-1)
            else: res.append(cur)
        return res   
