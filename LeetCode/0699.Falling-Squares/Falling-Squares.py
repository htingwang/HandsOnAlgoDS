class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        X = set()
        for x1, x2 in positions:
            X.add(x1)
            X.add(x1 + x2)
        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}
        root = Node(0, len(X) - 1)
        for x1, x2 in positions:
            h = root.query(Xi[x1], Xi[x1 + x2])
            #print(h)
            root.update(Xi[x1], Xi[x1 + x2], h + x2)
            #root.printall()
            #print(h)
            res.append(root.val)
        #root.printall()
        return res
        
class Node(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = self.right = None
        self.val = 0
        if e - s > 1:
            self.left = Node(s, (s + e) // 2)
            self.right = Node((s + e) // 2, e)
            
    def query(self, s, e): 
        #print(self.start, self.end, s, e, val)
        if s >= e: return 0
        if self.start == s and self.end == e:
            return self.val
        else:
            mid = (self.start + self.end) // 2    
            return max(self.left.query(s, min(mid, e)), self.right.query(max(mid, s), e))

    
    def update(self, s, e, val):
        #print(s, e, val)
        if s >= e: return
        if self.left:
            mid = (self.start + self.end) // 2
            self.left.update(s, min(mid, e), val)
            self.right.update(max(mid, s), e, val)
            self.val = max(self.left.val, self.right.val)
        else:
            self.val = val
    
    def printall(self):
        print(self.start, self.end, self.val)
        if self.left:
            self.left.printall()
            self.right.printall()
        
