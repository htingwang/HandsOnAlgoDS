class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evenidx = 1;
        for oddidx in range(0, len(A), 2):
            if (A[oddidx] % 2 == 1):
                while (A[evenidx] % 2 == 1):
                    evenidx += 2;
                A[oddidx], A[evenidx] = A[evenidx], A[oddidx]
        return A;
