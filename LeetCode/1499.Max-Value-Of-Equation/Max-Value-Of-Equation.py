class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        # maximize (yi - xi) + (xj + yj)
        return self.findMaxValueOfEquation3(points, k)
    
    # Stack. Time: O(n)
    def findMaxValueOfEquation3(self, points, k):
        res = float('-inf')
        queue = collections.deque()
        for x, y in points:
            while queue and x - queue[0][1] > k:
                queue.popleft()
            if queue: res = max(res, x + y + queue[0][0])
            while queue and queue[-1][0] <= y - x:
                queue.pop()
            queue.append((y - x, x))
        return res
    
    # Priority queue. Time: O(nlogn)
    def findMaxValueOfEquation2(self, points, k):
        res = float('-inf')
        minheap = []
        for x, y in points:
            while minheap and x - minheap[0][1] > k:
                heapq.heappop(minheap)
            if minheap: res = max(res, x + y - minheap[0][0])
            heapq.heappush(minheap, (x - y, x))
        return res
    
    def findMaxValueOfEquation1(self, points, k):
        n = len(points)
        minheap = []
        res = float('-inf')
        j = 1
        for i in range(n):
            while j < n and points[j][0] - points[i][0] <= k:
                heapq.heappush(minheap, (-points[j][0] - points[j][1], j))
                j += 1
            while minheap and minheap[0][1] <= i:
                heapq.heappop(minheap)
            if minheap: res = max(res, points[i][1] - points[i][0] - minheap[0][0])
        return res
