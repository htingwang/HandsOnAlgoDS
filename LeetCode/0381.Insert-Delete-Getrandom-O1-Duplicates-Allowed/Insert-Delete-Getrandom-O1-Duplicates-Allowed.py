class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.m = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.lst.append(val)
        self.m[val].add(len(self.lst) - 1)
        return len(self.m[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not len(self.m[val]): return False
        idx, last = self.m[val].pop(), len(self.lst) - 1
        self.lst[idx], self.lst[last] = self.lst[last], self.lst[idx]
        self.m[self.lst[idx]].add(idx)
        self.m[self.lst[idx]].remove(len(self.lst) - 1)
        
        self.lst.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
