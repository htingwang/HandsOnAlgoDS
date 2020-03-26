class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        i = j = 0
        num1 = num2 = 0
        for i in range(max(len(v1), len(v2))):
            cur1 = cur2 = 0
            if i < len(v1):
                cur1 = int(v1[i])
            if i < len(v2):
                cur2 = int(v2[i])
            if cur1 > cur2: return 1
            if cur2 > cur1: return -1
        return 0
