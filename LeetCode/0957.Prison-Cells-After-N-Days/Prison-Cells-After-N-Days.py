class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N == 0: return cells
        reverse = False
        idx = (N - 1) % 14
        if idx >= 7: reverse = True
        idx %= 7
        cells = self.prison_after_one_day(cells)
        res = []
        for i in range(idx):
            cells = self.prison_after_one_day(cells)
        if reverse: cells.reverse()    
        return cells
    
    def prison_after_one_day(self, cells):
        res = [0] * len(cells)
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]: res[i] = 1
        return res
