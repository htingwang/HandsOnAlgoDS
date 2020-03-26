class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0;
        for i in range(len(A[0])):
            for j in range(len(A) - 1):
                if (A[j+1][i] < A[j][i]): 
                    count += 1;
                    break;
        return count;
        
