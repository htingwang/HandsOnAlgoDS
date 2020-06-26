class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(words)
        while i < n:
            j = i
            cur = 0
            while j < n and cur + len(words[j]) + j - i <= maxWidth:
                cur += len(words[j])
                j += 1
 
            line = words[i]
            if j - i - 1 != 0:
                gap = (maxWidth - cur) / (j - i - 1)
                extra = (maxWidth - cur) % (j - i - 1)
                for k in range(i + 1, j):
                    if j == n:
                        line += " "
                    else:
                        if k - i <= extra:
                            line += " " * (gap + 1)
                        else:
                            line += " " * gap
                    line += words[k]
            line += " " * (maxWidth - len(line))
            res.append(line)
            i = j
        return res
