class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.nthUglyNumber2(n)
    
    def nthUglyNumber2(self, n):
        i2 = i3 = i5 = 0
        res = [1]
        for _ in range(n - 1):
            mn = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
            if mn == res[i2] * 2: i2 += 1
            if mn == res[i3] * 3: i3 += 1
            if mn == res[i5] * 5: i5 += 1
            res.append(mn)
        
        return res[-1]
        
        
    def nthUglyNumber1(self, n):
        minheap = [1]
        cnt = 1
        while minheap:
            if cnt == n: return minheap[0]
            cur = heapq.heappop(minheap)
            while minheap and cur == minheap[0]:
                heapq.heappop(minheap)
            cnt += 1
            heapq.heappush(minheap, cur * 2)
            heapq.heappush(minheap, cur * 3)
            heapq.heappush(minheap, cur * 5)
        return -1
            
        
