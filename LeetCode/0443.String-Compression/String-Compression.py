class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        if n == 1: return 1
        i = j = cur = 0
        while i < n:
            #print(i, j, n,  chars[i], chars[j], chars[j] == chars[i])
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[cur] = chars[i]
            cur += 1
            if j - i > 1:
                for c in str(j - i):
                    chars[cur] = c
                    cur += 1
            i = j
        return cur
