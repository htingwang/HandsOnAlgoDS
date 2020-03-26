class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1, f2 = 0, 0;
        for x in reversed(cost):
            tmp = f1;
            f1 = x + min(f1, f2);
            f2 = tmp;
        return min(f1, f2)
            
            
        
