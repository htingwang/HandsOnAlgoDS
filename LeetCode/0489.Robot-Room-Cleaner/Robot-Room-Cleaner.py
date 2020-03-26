# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def helper(robot, x, y, direction, visit):
            #print(x, y)
            robot.clean()
            visit.add((x, y))
            for i in range(4):
                cur = (i + direction) % 4
                nx, ny = x + di[cur][0], y + di[cur][1]
                if (nx, ny) not in visit and robot.move():
                    helper(robot, nx, ny, cur, visit)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnRight()
        di = [(1, 0), (0, 1), (-1, 0), (0, -1)]     
        visit = set()
        helper(robot, 0, 0, 0,  visit)
            
        
