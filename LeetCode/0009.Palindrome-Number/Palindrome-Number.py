class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        div = 1
        while x / div >= 10:
            div *= 10
            if x % div == 0: return False
        #print div
        while x > 0:
            #print x, div
            left = x / div
            right = x % 10
            if left != right:
                return False
            x = (x % div) / 10
            div = div / 100
        return True
