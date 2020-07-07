class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            duplicate = 1
            count = collections.defaultdict(int)
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2: 
                    duplicate += 1
                    continue
                dx, dy = x1 - x2, y1 - y2
                d = self.gcd(dx, dy)
                count[tuple((dx // d, dy // d))] += 1
            res = max(res, duplicate)
            for slope in count:
                res = max(res, count[slope] + duplicate)
                
        return res
        
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)
        
