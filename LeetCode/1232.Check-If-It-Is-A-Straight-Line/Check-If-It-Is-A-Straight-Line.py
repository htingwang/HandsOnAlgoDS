class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # y1 = ax1 + b
        # y2 = ax2 + b
        # a = (y1-y2)/(x1-x2)
        # b = y1 - a*x1
        # (x1-x2)y =(y1-y2)*x + (x1-x2) y1 - (y1-y2)*x1 
        if len(coordinates) == 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x1 - x2) * y != (y1 - y2) * x + (x1 - x2) * y1 - (y1 - y2) * x1:
                return False
        return True
        
