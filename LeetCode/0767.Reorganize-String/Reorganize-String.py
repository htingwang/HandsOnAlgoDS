class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = collections.Counter(S)
        maxheap = []
        for c in count:
            heapq.heappush(maxheap, (-count[c], c))
        if (-maxheap[0][0] > (len(S) + 1) / 2): return ""
        res = []
        while len(maxheap) > 1:
            f1, c1 = heapq.heappop(maxheap)
            f2, c2 = heapq.heappop(maxheap)
            res.append(c1)
            res.append(c2)
            if (f1 + 1 < 0):
                heapq.heappush(maxheap, (f1 + 1, c1))
            if (f2 + 1 < 0):
                heapq.heappush(maxheap, (f2 + 1, c2))
        if len(maxheap) > 0:
            f1, c1 = heapq.heappop(maxheap)
            res.append(c1)
        return "".join(res)




