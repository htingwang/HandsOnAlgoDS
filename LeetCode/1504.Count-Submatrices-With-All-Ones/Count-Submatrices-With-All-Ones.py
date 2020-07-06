class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        return self.numSubmat3(mat)
    
    # 1D Prefix sum + monotone increasing stack. Time: O(MN)
    def numSubmat3(self, mat):
        if not mat or not mat[0]: return 0
        res = 0
        m, n = len(mat), len(mat[0])
        count = [[0] * n for _ in range(m)]
        stack = [[] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if j and mat[i][j]: mat[i][j] += mat[i][j - 1]
                while stack[j] and mat[stack[j][-1]][j] >= mat[i][j]: stack[j].pop()
                pre_i, pre_count = -1, 0
                if stack[j]: pre_i, pre_count = stack[j][-1], count[stack[j][-1]][j]
                count[i][j] += pre_count + (i - pre_i) * mat[i][j]
                res += count[i][j]
                stack[j].append(i)
        return res
        
    # 1D Prefix sum. Time: O(MMN)
    def numSubmat2(self, mat): 
        if not mat or not mat[0]: return 0
        res = 0
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if j and mat[i][j]: mat[i][j] += mat[i][j - 1]
                w = float('inf')
                for k in range(i, -1, -1):
                    if mat[k][j] == 0: break
                    w = min(w, mat[k][j])
                    res += w
        return res
        
    # 2D Prefix sum. Time: O(MMNN)
    def numSubmat1(self, mat):
        if not mat or not mat[0]: return 0
        res = 0
        m, n = len(mat), len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        area = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + mat[i - 1][j - 1]
                area[i][j] = i * j
                
                
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: continue
                for w in range(1, m - i + 1):
                    for h in range(1, n - j + 1):
                        if pre[i + w][j + h] - pre[i + w][j] - pre[i][j + h] + pre[i][j] != area[w][h]:
                            break
                        res += 1
        return res
                        
        
