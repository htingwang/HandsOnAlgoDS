class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = address.replace(".", "[.]")
        #print(res)
        return res
