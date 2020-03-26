# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) / 2
            is_bad = isBadVersion(mid + 1)
            if is_bad:
                right = mid
            else:
                left = mid + 1
        return left + 1
        
