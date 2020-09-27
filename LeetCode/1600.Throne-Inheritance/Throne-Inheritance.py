class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.root = kingName
        self.inherit = collections.defaultdict(list)
        self.alive = {kingName: True}
        
        

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.inherit[parentName].append(childName)
        self.alive[childName] = True
        

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.alive[name] = False
        
    def dfs(self, name):
        res = []
        if self.alive[name]: res.append(name)
        for c in self.inherit[name]:
            res += self.dfs(c)
        return res
        
    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        return self.dfs(self.root)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
