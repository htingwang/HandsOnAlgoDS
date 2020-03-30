class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # pos(t) = start + speed * t
        # pos(0, t) = 10 + 2t = 12, t = 1
        # pos(1, t) =  8 + 4t = 12, t = 1
        # pos(3, t) =  5 +  t = 12, t = 7
        # pos(4, t) =  3 + 3t = 12, t = 3
        # pos(2, t) =  0 +  t = 12, t = 12
        
        heap = []
        n = len(position)
        for i in range(n):
            heapq.heappush(heap, (-position[i], speed[i]))
        res = cur = 0
        while heap:
            p_, s = heapq.heappop(heap)
            p = -p_
            time = float(target - p) / s
            #print(time)
            if time <= cur: continue
            res += 1
            cur = time
            
        return res
                           
            
