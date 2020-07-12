class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        def dist(x, y):
            return sum(sqrt((x - a) ** 2 + (y - b) ** 2) for a, b in positions)
        diff = 100
        x = sum(x for x, _ in positions) / float(len(positions))
        y = sum(y for _, y in positions) / float(len(positions))
        cur = dist(x, y)
        while diff > 1e-6:
            found = False
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + diff * dx, y + diff * dy
                new = dist(nx, ny)
                if new < cur:
                    cur = new
                    x, y = nx, ny
                    found = True
                    break
            if not found: diff /= float(2)
        return cur
                
            
        
