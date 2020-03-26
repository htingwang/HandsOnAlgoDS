class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.indexes = []
        

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.index = 0
    
    def insert(self, word):
        node =  self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node.indexes.append(self.index)
            node = node.children[c]
        node.is_word = True
        self.index += 1
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children: return False
            node = node.children[c]
        return node.is_word
    
    def is_start_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return False
            node = node.children[c]
        return True
    
    def start_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return []
            node = node.children[c]
        return node.indexes
    
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        dictionary = Trie()
        for word in words:
            dictionary.insert(word)
        res = []
        for word in words:
            self.helper(words, 1, dictionary, [word], res)
        return res
    
    def helper(self, words, level, trie, out, res):
        if level >= len(words[0]):
            res.append(out[:])
            return
        prefix = ""
        for i in range(level):
            prefix += out[i][level]
            
        indexes = trie.start_with(prefix)
        for index in indexes:
            out.append(words[index])
            self.helper(words, level + 1, trie, out, res)
            out.pop()
        return
