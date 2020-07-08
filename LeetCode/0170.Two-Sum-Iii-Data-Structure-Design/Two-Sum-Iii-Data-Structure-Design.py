class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.m[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.m:
            t = value - num
            if t in self.m:
                if (t == num and self.m[t] > 1) or (t != num and self.m[t] > 0): return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
