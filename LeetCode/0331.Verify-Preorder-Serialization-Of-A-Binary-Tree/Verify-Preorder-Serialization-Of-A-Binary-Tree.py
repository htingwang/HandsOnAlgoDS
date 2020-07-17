class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slot = 1
        for n in preorder.split(","):
            slot -= 1
            if slot < 0: return False
            if n != '#': slot += 2
        return slot == 0
