class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        done = False
        for i in range(len(A) - 2, -1, -1):
            tmp = idx = -1
            for j in range(i + 1, len(A)):
                if A[j] < A[i] and A[j] > tmp:
                    tmp = A[j]
                    idx = j
            #print(i, tmp, idx)
            if tmp != -1:
                A[i], A[idx] = A[idx], A[i]
                break
        return A
        
