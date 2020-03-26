class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        i, j = 0, 1
        ans = []
        while i < n or j < n:
            cur = len(words[i])
            while j < n and cur + len(words[j]) + 1 <= maxWidth:
                cur += (len(words[j]) + 1)
                j += 1
            extra1  = (maxWidth - cur)
            extra2 = 0
            tmp = words[i]
            if j - i - 1 == 0:
                tmp += " " * (maxWidth - cur)   
            else:
                extra1 = (maxWidth - cur) / (j - i - 1) + 1
                extra2 = (maxWidth - cur) % (j - i - 1)
                if j == n:
                    extra1, extra2 = 1, 0
                for k in range(i + 1, j):
                    if k - (i + 1) < extra2:
                        tmp += (" " * (extra1 + 1) + words[k])
                    else:
                        tmp += (" " * (extra1) + words[k])
            tmp = tmp + " " * (maxWidth - len(tmp))
            ans.append(tmp)
            i = j
            j += 1
        return ans
        
