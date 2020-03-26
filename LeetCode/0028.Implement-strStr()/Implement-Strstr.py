class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        if not m: return 0
        if not n: return -1
        
        kmp = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and needle[i] != needle[k]:
                k = kmp[k - 1]
            if needle[i] == needle[k]:
                k += 1
                kmp[i] = k
        k = 0        
        for i in range(n):
            while k > 0 and haystack[i] != needle[k]:
                k = kmp[k - 1]
            if haystack[i] == needle[k]:
                k += 1
            if k == m: return i - m + 1
        return -1
