class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        self.father = [i for i in range(N)]
        self.component = N
        logs.sort()
        
        for timestamp, a, b in logs:
            self.union(a, b)
            if self.component == 1:
                return timestamp
        return -1
        
    def find(self, a):
        x = a
        while self.father[x] != x:
            x = self.father[x]
        while self.father[a] != x:
            a, self.father[a] = self.father[a], x
        return x
    
    def union(self, a, b):
        A = self.find(a)
        B = self.find(b)
        if A != B:
            self.father[A] = B
            self.component -= 1
        
