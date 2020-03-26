class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        prefix_count = [[0] * 4 for _ in range(n + 1)]
        m = {"Q": 0, "W": 1, "E": 2, "R": 3}
        for i, c in enumerate(s):
            for j in range(4):
                prefix_count[i + 1][j] = prefix_count[i][j]
                if j == m[c]:
                    prefix_count[i + 1][j] += 1
                    
            
        avg = n // 4
        need_change = [0] * 4
        for i in range(4):
            if prefix_count[n][i] > avg:
                need_change[i] = prefix_count[n][i] - avg
        #print(need_change, avg)
        #print(prefix_count)
        if sum(need_change) == 0:
            return 0
        res = n
        def check():
            #print(i, j)
            if prefix_count[j + 1][0] - prefix_count[i][0] >= need_change[0]:
                    if prefix_count[j + 1][1] - prefix_count[i][1] >= need_change[1]:
                        if prefix_count[j + 1][2] - prefix_count[i][2] >= need_change[2]:
                            if prefix_count[j + 1][3] - prefix_count[i][3] >= need_change[3]:
                                return True
            return False
        i = j = 0
        while i < n and j < n:
            while j < n and check() == False:
                j += 1
            while i < n and j < n and check() == True:
                i += 1
            if i < n and j < n:
                #print(i, j)
                res = min(res, j - i + 2)
            i += 1
        return res
                    
