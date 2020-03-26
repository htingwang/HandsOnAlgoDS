class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        maps = {}
        for i in range(26):
            maps[chr(ord("a") + i)] = (i / 5, i % 5)
        #print(maps)
        
        i = j = 0
        res = ""
        for k, c in enumerate(target):
            ni, nj = maps[c]
            di, dj = ni - i, nj - j
            if k > 0 and target[k - 1] == "z" and di < 0:
                res += "U"
                di += 1
            if dj > 0: res += "R" * dj
            if dj < 0: res += "L" * (-dj)
            if di > 0: res += "D" * di
            if di < 0: res += "U" * (-di)
            res += "!"
            i, j = ni, nj
        return res
        
