class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if self.check(weights, mid) > D:
                left = mid + 1
            else:
                right = mid
        return right
    
    def check(self, weights, val):
        res = 1
        cur = 0
        for w in weights:
            cur += w
            if cur > val:
                res += 1
                cur = w
        return res
