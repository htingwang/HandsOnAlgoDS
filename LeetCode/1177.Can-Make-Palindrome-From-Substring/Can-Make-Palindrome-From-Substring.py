class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        cnt = [[0] * 26 for _ in range(len(s) + 1)]
        for i in range(len(s)):
            cnt[i + 1] = cnt[i][:]
            cnt[i + 1][ord(s[i]) - ord('a')] += 1
            
        res = []
        for q in queries:
            oddsum = 0
            for i in range(26):
                if (cnt[q[1] + 1][i] - cnt[q[0]][i]) % 2:
                    oddsum += 1
            res.append((oddsum // 2) <= q[2])
        return res
