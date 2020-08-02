class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.num = collections.deque(list(range(maxNumbers)))
        self.exist = set(list(range(maxNumbers)))
        

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.num: 
            res = self.num.popleft()
            self.exist.remove(res)
            return res
        return -1
        

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.exist
        

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if number in self.exist: return
        self.exist.add(number)
        self.num.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
