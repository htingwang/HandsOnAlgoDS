class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxzero = zero = leftzero = rightzero = 0;
        for i, seat in enumerate(seats):
            if seat == 0: zero += 1;
            else: zero = 0;
            if zero == i+1: 
                leftzero = zero;
            if i == len(seats)-1:
                rightzero = zero;
            maxzero = max(maxzero, zero, leftzero, rightzero);
        return max(leftzero, rightzero, (maxzero+1)/2);
            
        
