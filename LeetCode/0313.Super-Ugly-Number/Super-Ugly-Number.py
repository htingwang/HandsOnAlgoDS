class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        return self.nthSuperUglyNumber2(n, primes)
    
    def nthSuperUglyNumber2(self, n, primes):
        res = [1]
        idxs = [0] * len(primes)
        for _ in range(n - 1):
            mn, mn_i = float('inf'), 0
            for i, p in enumerate(primes):
                if p * res[idxs[i]] < mn:
                    mn, mn_i = p * res[idxs[i]], i

            res.append(mn)
            for i, p in enumerate(primes):
                if p * res[idxs[i]] == mn:
                    idxs[i] += 1
        return res[-1]
        
    def nthSuperUglyNumber1(self, n, primes):
        minheap = [1]
        count = 0
        while minheap:
            cur = heapq.heappop(minheap)
            while minheap and minheap[0] == cur: heapq.heappop(minheap)
            count += 1
            if count == n: return cur
            for p in primes:
                heapq.heappush(minheap, cur * p)
        return -1
        
