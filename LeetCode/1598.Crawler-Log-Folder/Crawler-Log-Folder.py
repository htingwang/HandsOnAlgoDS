class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        
        d = 0
        for l in logs:
            if l == "../":
                d = max(0, d - 1)
            elif l != "./":
                d += 1
        return d
        
