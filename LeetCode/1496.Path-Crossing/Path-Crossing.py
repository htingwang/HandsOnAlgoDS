class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        direction = {'N':(0, 1), 'S':(0, -1), 'E':(1, 0), 'W': (-1, 0)}
        seen = set([(0, 0)])
        i, j = 0, 0
        for d in path:
            i += direction[d][0]
            j += direction[d][1]
            if (i, j) in seen: return True
            seen.add((i, j))
        return False
                   
        
        
