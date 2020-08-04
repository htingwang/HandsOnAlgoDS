class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.m = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.m: return False
        self.lst.append(val)
        self.m[val] = len(self.lst) - 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.m: return False
        idx, last = self.m[val], len(self.lst) - 1
        self.lst[idx], self.lst[last] = self.lst[last], self.lst[idx]
        self.m[self.lst[idx]] = idx
        del self.m[val]
        self.lst.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
