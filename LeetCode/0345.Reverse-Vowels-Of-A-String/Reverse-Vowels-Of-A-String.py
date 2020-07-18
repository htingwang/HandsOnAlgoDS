class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        left, right = 0, len(a) - 1
        v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        
        while left < right:
            while left < len(a) and a[left] not in v: left += 1
            while right >= 0 and a[right] not in v: right -= 1
            if left >= right: break
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        return "".join(a)
