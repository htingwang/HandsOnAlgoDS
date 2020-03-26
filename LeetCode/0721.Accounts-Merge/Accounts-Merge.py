from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        self.father = [i for i in range(n)]
        
        email_to_idxs = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_idxs[email].append(i)
        for email in email_to_idxs:
            idxs = email_to_idxs[email]
            for i in range(1, len(idxs)):
                self.union(idxs[0], idxs[i])
        idx_to_emails = defaultdict(set)
        for i, account in enumerate(accounts):
            root = self.find(i)
            for email in account[1:]:
                idx_to_emails[root].add(email)
        ans = [[] for _ in range(len(idx_to_emails))]
        for i, idx in enumerate(idx_to_emails):
            ans[i].append(accounts[idx][0])
            for email in sorted(idx_to_emails[idx]):
                ans[i].append(email) 
        return ans
        
    def union(self, a, b):
        self.father[self.find(a)] = self.find(b)
    def find(self, a):
        x = a
        while self.father[x] != x:
            x = self.father[x]
        while self.father[a] != x:
            a, self.father[a] = self.father[a], x
        return x
