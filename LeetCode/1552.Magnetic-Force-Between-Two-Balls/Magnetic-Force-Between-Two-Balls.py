class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        n = len(position)
        def count(d):
            res = 1
            cur = position[0]
            for i in range(1, n):
                if position[i] - cur >= d:
                    res += 1
                    cur = position[i]
            return res
        
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = left + (right - left) // 2
            if count(mid) >= m:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
            
