class Solution(object):
    def mask_vowel(self, word):
        word_array = list(word)
        for i, c in enumerate(word_array):
            if c in "aeiou":
                word_array[i] = "*"
        return "".join(word_array)
                
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        word_set = set(wordlist)
        word_cap = {}
        word_mask_vowel = {}
        
        for word in wordlist:
            word_low = word.lower()
            if word_low not in word_cap:
                word_cap[word_low] = word
            if self.mask_vowel(word_low) not in word_mask_vowel:
                word_mask_vowel[self.mask_vowel(word_low)] = word

        res = []
        for q in queries:
            if q in word_set:
                res.append(q)
            elif q.lower() in word_cap:
                res.append(word_cap[q.lower()] )
            elif self.mask_vowel(q.lower()) in word_mask_vowel:
                res.append(word_mask_vowel[self.mask_vowel(q.lower())])
            else:
                res.append("")
        return res
