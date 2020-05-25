class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # 0000(0), 0001(1), 0010(2), 0011(3), 0100(4), 0101(5), 0110(6), 0111(7)
        # 1000(8), 1001(9), 1010(10), 1011(11), 1100(12), 1101(13), 1110(14), 1111(15)
        return self.isRectangleCover3(rectangles)
    
    # Line sweep. Time/Space: O(N^2). If using treeset(available in java), O(NlogN)
    def isRectangleCover3(self, rectangles):
        area = 0
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        xpoints = []
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            area += (x2 - x1) * (y2 - y1)
            xpoints.append((x1, 1, y1, y2))
            xpoints.append((x2, -1, y1, y2))
        #if area != (max_x - min_x) * (max_y - min_y): return False
        xpoints.sort()
        ypoints = []
        ylen = 0
        for i, (x, s, y1, y2) in enumerate(xpoints):
            if s > 0:
                j = bisect.bisect_left(ypoints, (y1, y2))
                bisect.insort_left(ypoints, (y1, y2))
                if (j > 0 and ypoints[j - 1][1] > y1) or (j + 1 < len(ypoints) and ypoints[j + 1][0] < y2): return False
                ylen += (y2 - y1)
            else:
                ypoints.remove((y1, y2))
                ylen -= (y2 - y1)
                
            if i < len(xpoints) - 1 and x != xpoints[i + 1][0] and ylen != max_y - min_y: return False
                
            
        return True
    
    # Time/Space: O(N)
    def isRectangleCover2(self, rectangles):
        points = set()
        area = 0
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            area += (x2 - x1) * (y2 - y1)
            if tuple((x1, y1)) in points: points.remove(tuple((x1, y1)))
            else: points.add((tuple((x1, y1))))
            if tuple((x1, y2)) in points: points.remove(tuple((x1, y2)))
            else: points.add((tuple((x1, y2))))
            if tuple((x2, y1)) in points: points.remove(tuple((x2, y1)))
            else: points.add((tuple((x2, y1))))
            if tuple((x2, y2)) in points: points.remove(tuple((x2, y2)))
            else: points.add((tuple((x2, y2))))
        
        if tuple((min_x, min_y)) not in points: return False
        if tuple((min_x, max_y)) not in points: return False
        if tuple((max_x, min_y)) not in points: return False
        if tuple((max_x, max_y)) not in points: return False

        return len(points) == 4 and area == (max_x - min_x) * (max_y - min_y)    
        
    # Bit Manipulation. Time/Space: O(N)
    def isRectangleCover1(self, rectangles):
        m = collections.defaultdict(int)
        area = 0
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            area += (x2 - x1) * (y2 - y1)
            if not self.valid(m, tuple((x1, y1)), 1): return False
            if not self.valid(m, tuple((x1, y2)), 2): return False
            if not self.valid(m, tuple((x2, y1)), 4): return False
            if not self.valid(m, tuple((x2, y2)), 8): return False
        
        cnt = 0
        for val in m.values():
            if val not in set([3, 5, 6, 9, 10, 12, 15]): cnt += 1

        return cnt == 4 and area == (max_x - min_x) * (max_y - min_y)
    
    def valid(self, m, p, v):
        if m[p] & v: return False
        m[p] |= v
        return True
            
            
        
