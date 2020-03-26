class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        bal = collections.defaultdict(int)
        for a, b, c in transactions:
            bal[a] -= c
            bal[b] += c
        bal_list = [bal[i] for i in bal if bal[i] != 0]
        
        self.res = float('inf')
        self.dfs(bal_list, 0, 0)
        return self.res
    
    def dfs(self, bal, start, cnt):
        while start < len(bal) and bal[start] == 0: start += 1
        if start == len(bal):
            self.res = min(self.res, cnt)
            return
        prev = 0
        for i in range(start + 1, len(bal)):
            if (prev != bal[i] and bal[i] * bal[start] < 0):
                bal[i] += bal[start]
                self.dfs(bal, start + 1, cnt + 1)
                bal[i] -= bal[start]
            prev = bal[i] 
