class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.frequencySort2(s)
    
    # hash table + priority queue: O(nlogn)
    def frequencySort1(self, s):
        res = ""
        count = collections.Counter(s)
        maxheap = []
        for c in count:
            heapq.heappush(maxheap, (-count[c], c))
        while maxheap:
            freq, c = heapq.heappop(maxheap)
            res += c * (-freq)
        return res
    
    # bucket sort: O(n)
    def frequencySort2(self, s):
        if not s: return s
        res = ""
        count = collections.Counter(s)
        max_freq = max(count.values() )
        bucket = [[] for _ in range(max_freq + 1)]
        for c in count:
            bucket[count[c]].append(c)
        for i in range(max_freq, 0, -1):
            for c in  bucket[i]: res += c * i
        return res


