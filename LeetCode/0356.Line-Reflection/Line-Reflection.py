class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        mx, mn = float('-inf'), float('inf')
        m = collections.defaultdict(set)
        for x, y in points:
            m[x].add(y)
            mx = max(mx, x)
            mn = min(mn, x)
        mid = (mx + mn) / float(2)
        
        for x, y in points:
            rx = 2 * mid - x
            if not m[rx] or y not in m[rx]: return False
        
        return True
