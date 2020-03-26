class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = ""
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.index = 0
        
    def insert(self, word):
        node = self.root
        #print("insert " + word)
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        #print(word)
        node.word = word
    
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        dictionary = Trie()
        for word in words:
            dictionary.insert(word)
        res = []
        node = dictionary.root
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.helper(board, i, j, node, res)   
        return list(set(res))
    
    def helper(self, board, i, j, node, res):
        if board[i][j] not in node.children: return
        node = node.children[board[i][j]]    
        if node.word:
            res.append(node.word)
        tmp = board[i][j]
        board[i][j] = "*"
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != "*":
                self.helper(board, ni, nj, node, res)
        board[i][j] = tmp
        return  
