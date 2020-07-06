class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        return max(max(left) if left else 0, n - min(right) if right else 0)
    # -> <-
    # <- ->
