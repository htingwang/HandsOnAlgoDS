import collections
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.freq[x] += 1
        if self.freq[x] > self.max_freq:
            self.max_freq = self.freq[x]
        self.group[self.freq[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        num = self.group[self.max_freq].pop()
        self.freq[num] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
