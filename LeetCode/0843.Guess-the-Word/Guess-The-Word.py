# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        count = collections.defaultdict(int)
        for i in range(len(wordlist)):
            for j in range(len(wordlist)):
                if i != j and self.match(wordlist[i], wordlist[j]) == 0:
                    count[wordlist[i]] += 1
        #print(count)
        while True:
            guess = min(wordlist, key = lambda w: count[w])
            n = master.guess(guess)
            #print(guess, n)
            if n == 6: break
            wordlist = [word for word in wordlist if self.match(word, guess) == n]
    def match(self, w1, w2):
        res = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]: res += 1
        #print(w1, w2, res)
        return res
    

