class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)/4):
            for j in range(3):
                for k in range(j+1,4):
                    if A[i*4 + j] == A[i*4 + k]:
                        return A[i*4 + k];

        
