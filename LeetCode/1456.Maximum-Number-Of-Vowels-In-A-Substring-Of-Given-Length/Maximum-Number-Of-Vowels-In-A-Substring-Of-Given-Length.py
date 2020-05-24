class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        v = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        res = 0
        for i, c in enumerate(s):
            if c in v: cnt += 1
            res = max(res, cnt)
            if i >= k - 1:
                if s[i - k + 1] in v: cnt -= 1
        return res
