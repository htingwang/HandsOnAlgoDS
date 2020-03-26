class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n1, s1 = 0, 1
        n = len(A)
        for i in range(1, n):
            n2, s2 = float('inf'), float('inf')
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)
            n1, s1 = n2, s2
        return min(n1, s1)
        
