class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True
            
        for i in range(len(text)):
            j = i
            node = root
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                if node.is_word: res.append([i, j])
                j += 1
                
        res.sort()
        return res
        
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
