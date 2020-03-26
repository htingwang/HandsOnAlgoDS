import heapq
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        def dis(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        
        res = [-1] * len(workers)
        distances = []
        
        for i in range(len(workers)):
            cur = []
            for j in range(len(bikes)):
                cur.append([dis(i, j), i, j])
            tmp = cur[:]
            heapq.heapify(tmp)
            heapq.heappush(distances, tmp)
                
        used_b = set()
        
        
        n = 0
        while n < len(res):
            cur = heapq.heappop(distances)
            d = i = j = -1
            d, i, j = heapq.heappop(cur)
            if j in used_b: 
                heapq.heappush(distances, cur)
                continue
            used_b.add(j)
            #print(distances)
            res[i] = j
            n += 1
        return res
            
