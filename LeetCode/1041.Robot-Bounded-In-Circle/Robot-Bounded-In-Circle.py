class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        posx, posy = 0,0;
        dirx, diry = 0,1;
        for i in range(4):
            for x in instructions:
                if x == "G":
                    posx, posy = posx+dirx, posy+diry;
                    #print [posx, posy, dirx, diry]
                elif x == "L":
                    dirx, diry = -diry, dirx;
                elif x == "R":
                    dirx, diry = diry, -dirx;
        return (posx, posy)==(0, 0) or (dirx, diry) != (0, 1);
                     
        
