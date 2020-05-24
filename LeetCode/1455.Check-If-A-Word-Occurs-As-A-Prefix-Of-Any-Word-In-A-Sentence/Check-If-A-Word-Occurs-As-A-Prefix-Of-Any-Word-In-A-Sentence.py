class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        strs = sentence.split(" ")
        for i, s in enumerate(strs):
            cnt = 0
            for j, c in enumerate(searchWord):
                if j >= len(s): break
                if c == s[j]: cnt += 1
            if cnt == len(searchWord): return i + 1
        return -1
