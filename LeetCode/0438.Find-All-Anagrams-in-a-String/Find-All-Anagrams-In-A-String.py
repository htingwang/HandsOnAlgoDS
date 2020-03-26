import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s: return []
        res = []
        n = len(p)
        pivot = len(set(p))
        count = collections.Counter(p)
        cur = 0
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    cur += 1
            if cur == pivot:
                res.append(i - n + 1)
            if i >= n - 1:
                if s[i - n + 1] in count:
                    count[s[i - n + 1]] += 1
                    if count[s[i - n + 1]] == 1:
                        cur -= 1
        return res
