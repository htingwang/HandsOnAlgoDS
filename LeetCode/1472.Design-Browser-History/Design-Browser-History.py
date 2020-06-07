class node(object):
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None
        
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.cur = node(homepage)
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new = node(url)
        self.cur.next = new
        new.prev = self.cur
        self.cur = new

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0:
            if self.cur.prev == None: break
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.name

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0:
            if self.cur.next == None: break
            self.cur = self.cur.next
            steps -= 1
        return self.cur.name
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
