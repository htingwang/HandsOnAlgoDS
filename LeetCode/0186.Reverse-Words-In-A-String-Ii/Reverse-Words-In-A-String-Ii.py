class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        for i in range(n):
            if i == n - 1 or s[i + 1] == ' ':
                self.reverse(s, left, i)
                left = i + 2
        self.reverse(s, 0, n - 1)
           
    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        
