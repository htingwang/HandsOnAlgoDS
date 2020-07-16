class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dict = collections.defaultdict(set)
        for word in dictionary:
            if word: self.dict[word[0] + str(len(word) - 2) + word[-1]].add(word) 
                
    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word: return True
        key = word[0] + str(len(word) - 2) + word[-1]
        
        if word in self.dict[key]: return len(self.dict[key]) == 1
        else: return len(self.dict[key]) == 0


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
