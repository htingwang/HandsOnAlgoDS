class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        bit = [0] * (n + 1)
        toidx = collections.defaultdict(list)
        for i in range(n - 1, -1, -1): toidx[num[i]].append(i)
        
        def update(i):
            i += 1
            while i <= n:
                bit[i] += 1
                i += (i & -i)
            
        def get(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= (i & -i)
            return res
                
        def find():
            for n in range(10):
                if not toidx[str(n)]: continue
                i = toidx[str(n)][-1]
                cost = i - get(i)
                if cost <= k:
                    toidx[str(n)].pop()
                    return cost, i
            return 0, -1
        
        remove = [False] * n
        res = []
        while k:
            cost, i = find()
            if i == -1: break
            res.append(num[i])
            remove[i] = True
            update(i)
            k -= cost

        for i in range(n):
            if not remove[i]: res.append(num[i])

        return "".join(res)
