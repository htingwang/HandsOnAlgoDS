class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #[3,2,4,1]
        #3,[4,2,3,1]
        #4,[1,3,2,4]
        #2,[3,1,2,4]
        #3,[2,1,3,4]
        #2,[1,2,3,4]
        flips = [];
        B= sorted(A);
        C = sorted(range(1, len(A)+1), key = lambda i: -A[i-1]);
        print C
        i = len(A)-1;
        while i > 0:
            if A[i] == B[i]:
                i-= 1;
            else:
                left,right=0, A.index(B[i]);
                if right != 0:
                    flips.append(right+1);
                    while left < right:
                        A[left], A[right] = A[right], A[left];
                        left += 1;
                        right -= 1;
                #print A
                left, right=0, i;
                flips.append(i+1);
                while left < right:
                    A[left], A[right] = A[right], A[left];                               left += 1;
                    right -= 1;    
                #print A
        return flips;
        
