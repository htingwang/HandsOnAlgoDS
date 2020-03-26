class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        self.quickSelect(points, 0, len(points) - 1, K)
        return points[: K]
        res = []
        for i in range(K):
            res.append(points[i])
        return res
    
    def quickSelect(self, points, start, end, K):
        if start >= end: return
        left, right = start, end
        mid = (left + right) // 2
        pivot = points[mid][0] ** 2 + points[mid][1] ** 2
        while left <= right:
            while left <= right and points[left][0] ** 2 + points[left][1] ** 2 < pivot:
                left += 1
            while left <= right and points[right][0] ** 2 + points[right][1] ** 2 > pivot:
                right -= 1
            if left <= right:
                points[left], points[right] = points[right], points[left]
                left += 1
                right -= 1
        if start + K - 1 <= right:
            return self.quickSelect(points, start, right, K)
        if start + K - 1 >= left:
            return self.quickSelect(points, left, end, K - (left - start))
        return
