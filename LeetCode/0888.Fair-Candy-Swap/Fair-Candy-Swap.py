class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = sum(A) - sum(B);
        diff /= 2;
        exists = {};
        for i in range(len(A)):
            exists[A[i]-diff] = exists.get(A[i]-diff, 0)+1;
        for i in range(len(B)):
            if exists.get(B[i], 0) != 0: break;
        return [B[i]+diff, B[i]] 
