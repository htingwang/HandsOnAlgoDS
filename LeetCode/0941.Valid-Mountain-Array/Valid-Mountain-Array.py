class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        left, right = 0, len(A)-1;
        while left < right and left < len(A)-1 and right > 0:
            if A[left+1] == A[left] or A[right-1] == A[right]:
                return False;
            if A[left+1] < A[left] and A[right-1] < A[right]:
                return False;
            if A[left+1] > A[left]: left += 1;
            if A[right-1] > A[right]: right -= 1;
        return left == right and left!=0 and left!=len(A)-1;
        
        
