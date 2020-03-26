class TrieNode(object):
    
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_node(self.root, word)
        
    def search_node(self, node, word):
        if not word:
            return node.is_word
        if word[0] == ".":
            for c in node.children:
                if self.search_node(node.children[c], word[1:]):
                    return True
        else:
            if word[0] in node.children:
                return self.search_node(node.children[word[0]], word[1:])
        return False
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
