class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0;
        right = len(A) - 1;
        i = right;
        B = [0]*len(A);
        while i > -1:
            if (A[right] ** 2 >= A[left] ** 2):
                B[i] = A[right] ** 2;
                right = right-1;
            else:
                B[i] = A[left] ** 2;
                left = left + 1;
            i = i - 1;
        return B;
            
        
