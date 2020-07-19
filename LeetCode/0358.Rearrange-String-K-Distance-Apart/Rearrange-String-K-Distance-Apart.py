class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0: return s
        res = ""
        m = collections.defaultdict(int)
        for c in s: m[c] += 1
        maxheap = []
        for c in m: heapq.heappush(maxheap, (-m[c], c))
        left = len(s)
        while maxheap:
            cnt = min(left, k)
            v = []
            for _ in range(cnt):
                if not maxheap: return ""
                n, c = heapq.heappop(maxheap)
                res += c
                if n + 1 != 0: v.append(((n + 1), c))
            left -= cnt
            for a in v: heapq.heappush(maxheap, a)
        return res
