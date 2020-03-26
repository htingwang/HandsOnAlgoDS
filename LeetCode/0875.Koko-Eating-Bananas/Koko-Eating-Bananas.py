class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right ) // 2
            if self.check(piles, mid) > H:
                left = mid + 1
            else:
                right = mid
        return right
    
    def check(self, piles, k):
        res = 0
        for p in piles:
            res += math.ceil(float(p) / k)
        return res
