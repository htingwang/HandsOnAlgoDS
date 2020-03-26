class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ans = -1
        A.sort()
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] + A[right] >= K:
                right -= 1
            else:
                #print(A, left, right)
                while left < right and A[left] + A[right] < K:
                    ans = max(ans, A[left] + A[right])
                    left += 1
        return ans
        
