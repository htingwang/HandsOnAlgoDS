class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        #     x(1)
        #    ┌───┐
        #x(2)│   │x(0)
        #    └───┼──>
        #     x(3)
        
        #      x(1)
        #    ┌──────┐
        #    │      │x(0)
        #x(2)│      ^
        #    │      │x(4)
        #    └──────│
        #      x(3)
        
        #     x(1)
        #    ┌──────┐
        #    │      │x(0)
        #x(2)│     <│────│
        #    │       x(5)│x(4)
        #    └───────────│
        #        x(3)
        
        n = len(x)
        for i in range(3, n):
            if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]: return True
            elif i >= 4 and x[i - 3] == x[i - 1] and x[i - 4] + x[i] >= x[i - 2]: return True
            elif i >= 5 and x[i - 4] <= x[i - 2] and x[i - 4] + x[i] >= x[i - 2] and x[i - 1] <= x[i - 3] and x[i - 5] + x[i - 1] >= x[i - 3]: return True
        return False
        
