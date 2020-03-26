class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def dis(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        minheap = [[0, 0, 0]]
        seen = set()
        while True:
            d, w, taken = heapq.heappop(minheap)
            if taken in seen: continue
            seen.add(taken)
            #print(d, w, taken)
            if w == len(workers): return d
            for j in range(len(bikes)): 
                if taken & (1 << j) == 0:
                    heapq.heappush(minheap, [d + dis(w, j), w + 1, taken | (1 << j)])
