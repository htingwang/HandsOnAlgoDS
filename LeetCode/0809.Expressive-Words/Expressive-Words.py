class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            if self.check(S, word): res += 1
        return res
    
    def check(self, S, word):
        if word == S: return True
        i = j = 0
        while i < len(word) and j < len(S):
            if word[i] != S[j]: return False
            cnt1 = cnt2 = 0
            while i < len(word) - 1 and word[i] == word[i + 1]:
                cnt1 += 1
                i += 1
            while j < len(S) - 1 and S[j] == S[j + 1]:
                cnt2 += 1
                j += 1
            #print(cnt1, cnt2)
            if cnt1 != cnt2 and cnt2 < 2: return False
            if cnt1 > cnt2: return False
            i += 1
            j += 1
        #print(i, j)
        return i == len(word) and j == len(S)
        
        
