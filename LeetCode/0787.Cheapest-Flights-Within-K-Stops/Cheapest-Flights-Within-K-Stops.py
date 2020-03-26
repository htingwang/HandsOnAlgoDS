class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for f in flights:
            graph[f[0]].append((f[1], f[2]))
        
        res = float('inf')
        queue = collections.deque()
        queue.append((src, 0))
        for i in range(K + 2):
            size = len(queue)
            for j in range(size):
                cur, cost = queue.popleft()
                if cur == dst:
                    res = min(res, cost)
                for k in range(len(graph[cur])):
                    if cost + graph[cur][k][1] >= res:
                        continue
                    queue.append((graph[cur][k][0], cost + graph[cur][k][1])) 
                    #print(i, queue)
        return res if res != float('inf') else -1
