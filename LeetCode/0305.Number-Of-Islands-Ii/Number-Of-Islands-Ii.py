class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.father = {}
        self.size = 0
        ans = []
        for i, j in positions:
            self.insert(i * n + j)
            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni * n + nj) in self.father:
                        self.union(ni * n + nj, i * n + j)
            ans.append(self.size)
        return ans
        
    def insert(self, a):
        if a not in self.father:
            self.father[a] = a
            self.size += 1
        
    def union(self, a, b):
        A = self.find(a)
        B = self.find(b)
        if A != B:
            self.father[A] = B
            self.size -= 1
            
    def find(self, a):
        x = a
        while self.father[x] != x:
            x = self.father[x]
        while self.father[a] != x:
            a, self.father[a] = self.father[a], x
        return x
    
        
        
