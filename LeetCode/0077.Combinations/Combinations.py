class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(first = 1, cur = []):
            if len(cur) == k: ans.append(cur[:])
            for i in range(first,  n + 1):
                cur.append(i)
                #print first, i, cur
                backtrack(i + 1, cur)
                cur.pop()
        ans = []
        backtrack()
        return ans
