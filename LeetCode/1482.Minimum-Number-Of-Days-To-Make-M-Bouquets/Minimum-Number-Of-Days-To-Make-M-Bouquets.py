class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay): return -1
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if self.check(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return right
    
    def check(self, bloomDay, m, k, mid):
        flow = bou = 0
        for d in bloomDay:
            if d <= mid:
                flow += 1
                if flow == k:
                    bou += 1
                    flow = 0
                    if bou == m: return True
            else:
                flow = 0
        return False
