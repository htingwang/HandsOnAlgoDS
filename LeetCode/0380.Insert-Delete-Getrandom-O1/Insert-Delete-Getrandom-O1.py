class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.exists = set();
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.exists:
            return False;
        else:
            self.exists.add(val);
            return True;
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.exists:
            self.exists.remove(val);
            return True;
        return False;

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        #print self.stack
        return random.sample(self.exists, 1)[0];
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
