class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.reverseWords2(s)
    
    def reverseWords2(self, s):
        return " ".join(reversed(s.split()))
        
        
    def reverseWords1(self, s):
        s = s.strip(' ')
        queue = collections.deque()
        left = 0
        for i, c in enumerate(s):
            if i > 0 and s[i - 1] == ' ': left = i
            if i == len(s) - 1 or (s[i + 1] == ' ' and s[i] != ' '):
                queue.appendleft(s[left : i + 1])
            
        return " ".join(queue)
