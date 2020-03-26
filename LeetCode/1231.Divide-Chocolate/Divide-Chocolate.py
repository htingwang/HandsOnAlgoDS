class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        left, right = min(sweetness), sum(sweetness)
        while left < right:
            mid = (left + right + 1) // 2
            if self.check(sweetness, mid) < (K + 1):
                right = mid - 1
            else:
                left = mid
        return left
    
    def check(self, sweetness, val):
        cur = res = 0
        for s in sweetness:
            cur += s
            if cur >= val:
                res += 1
                cur = 0
        return res
