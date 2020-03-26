class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        row, col = king[0], king[1]
        qweens_set = set()
        for x, y in queens:
            qweens_set.add((x, y))
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for di, dj in directions:
            ni, nj = king[0] + di, king[1] + dj
            while 0 <= ni < 8 and 0 <= nj < 8:
                if (ni, nj) in qweens_set:
                    res.append([ni, nj])
                    break
                ni += di
                nj += dj
        return res
