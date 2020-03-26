class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        rescount = [1] + [0]*(K-1);
        for i in range(len(A)):
            if i > 0: A[i] += A[i-1];
            rescount[A[i] % K] += 1;
        return sum(n*(n-1)/2 for n in rescount);
