class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc, preinc = -1, -1;
        for i in range(len(A)-1):
            if (A[i+1] > A[i]): inc = 1;
            elif (A[i+1] < A[i]): inc = 0;
            if (preinc + inc) == 1: return False;
            preinc = inc;
        return True;
        
