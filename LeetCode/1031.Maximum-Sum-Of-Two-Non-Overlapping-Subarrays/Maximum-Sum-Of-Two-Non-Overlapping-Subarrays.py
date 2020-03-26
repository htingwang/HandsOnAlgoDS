class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        for i in range(1,len(A)):
            A[i] += A[i-1];
        ans, maxL, maxM = A[L+M-1], A[L-1], A[M-1];
        for i in range(L+M, len(A)):
            maxL = max(maxL, A[i-M]-A[i-M-L]);
            maxM = max(maxM, A[i-L]-A[i-L-M]);
            ans = max(ans, max(maxL+A[i]-A[i-M], maxM+A[i]-A[i-L]));
        return ans;
