class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)

        def next_idx(idxs, n):
            stack = []
            res = [-1] * n
            for idx in idxs:
                while stack and stack[-1] < idx:
                    res[stack.pop()] = idx
                stack.append(idx)
            return res
        
        idx_inc = sorted(range(n), key = lambda i: A[i])
        odd_next = next_idx(idx_inc, n)
        idx_dec = sorted(range(n), key = lambda i: -A[i])
        even_next = next_idx(idx_dec, n)
        
        odd = [False] * n
        even = [False] * n
        odd[n - 1] = even[n - 1] = True

        for i in range(n - 2, -1, -1):
            if odd_next[i] != -1:
                odd[i] = even[odd_next[i]]
            if even_next[i] != -1:
                even[i] = odd[even_next[i]]

        return sum(odd)       
