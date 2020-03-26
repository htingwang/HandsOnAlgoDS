class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.times = 0
        
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.cur = ""
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])
        
    def insert(self, sentence, times):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.times += times
        
    def lookup(self, sentence):
        node = self.root
        for c in sentence:
            if c not in node.children:
                return []
            node = node.children[c]
        res = []
        self.traverse(node, sentence, res)
        return res
    
    def traverse(self, node, sentence, res):
        if node.times:
            res.append((node.times, sentence))
        for c in node.children:
            self.traverse(node.children[c], sentence + c, res)
    
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.insert(self.cur, 1)
            self.cur = ""
            return []
        self.cur += c
        candidates = self.lookup(self.cur)
        candidates.sort(key = lambda x:(-x[0], x[1]))
        #print(self.cur, candidates)
        res = []
        for i in range(min(len(candidates), 3)):
            res.append(candidates[i][1])
        return res
        
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
