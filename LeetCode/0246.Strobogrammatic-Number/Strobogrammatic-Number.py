class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        m = {'6': '9', '8': '8', '9': '6', '1': '1', '0': '0'}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in m or m[num[left]] != num[right]: return False
            left += 1
            right -= 1

        return True
