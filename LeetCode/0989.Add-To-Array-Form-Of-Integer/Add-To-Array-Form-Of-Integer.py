class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        ans = [];
        i = len(A)-1
        carrier = K;
        while i >= 0 or carrier > 0:
            #print(carrier)
            if (i >= 0): carrier += A[i];
            ans.insert(0, (carrier)%10);
            carrier = carrier/10;
            i -= 1;
        return ans;
