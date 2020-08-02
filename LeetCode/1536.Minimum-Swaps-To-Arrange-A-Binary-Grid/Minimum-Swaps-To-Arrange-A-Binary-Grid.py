class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        zero = [0] * n
        count = collections.defaultdict(int)
        for i in range(n):
            cnt = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1: break
                cnt += 1
            cnt = min(cnt, n - 1)
            zero[i] = cnt
            count[cnt] += 1
        cnt = n - 1
        for i in range(n):
            while not count[cnt]: cnt -= 1
            count[cnt] -= 1
            if n - 1 - i > cnt: return -1

        res = 0
        for i in range(n):
            if zero[i] >= n - 1 - i: continue
            j = i + 1
            while zero[j] < n - 1 - i:
                j += 1
            res += j - i
            while j > i:
                zero[j], zero[j - 1] = zero[j - 1], zero[j]
                j -= 1   
        return res
            
        
        
                
