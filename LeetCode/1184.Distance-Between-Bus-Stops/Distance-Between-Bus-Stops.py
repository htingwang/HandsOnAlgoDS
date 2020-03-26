class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        n = len(distance)
        s = [0] * (n + 1)
        
        for i in range(n):
            s[i + 1] = s[i] + distance[i]
        
        if start > destination:
            start, destination = destination, start
        candidate = s[destination] - s[start]
        return min(candidate, s[n] - candidate)
        
