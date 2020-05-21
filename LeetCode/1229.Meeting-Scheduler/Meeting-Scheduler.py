class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        minheap = []
        for t in slots1 + slots2:
            if True:#t[1] - t[0] >= duration:
                heapq.heappush(minheap, t)
        while len(minheap) > 1:
            s, e = heapq.heappop(minheap)
            ns, ne = minheap[0]
            if (e >= ns + duration and ne - ns >= duration):
                return [ns, ns + duration]
        return []


