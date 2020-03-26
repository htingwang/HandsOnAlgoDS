class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if sum(A)%3 != 0: return False;
        
        subsum = sum(A)/3;
        accsum = 0;
        check = 0;
        for a in A:
            accsum += a;
            if accsum == subsum:
                check += 1;
                accsum = 0;
            if check == 2:
                break;
        return (check == 2);
            
            
