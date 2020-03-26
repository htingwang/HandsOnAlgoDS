class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0,  len(A) - 1
        while left < right:
            mid = (left + right) // 2
            #print(left, right, mid)
            if A[mid] >= mid:
                right = mid
            else:
                left = mid + 1
        if A[left] == left: return left
        return -1
        
