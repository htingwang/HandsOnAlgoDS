class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        invalid = set(["2", "3", "4", "5", "7"])
        numstr = str(N)
        if set(numstr).intersection(invalid): return False
        
        left, right = 0, len(numstr) - 1
        while left < right:
            if mapping[numstr[left]] != numstr[right]: return True
            left += 1
            right -= 1
        if left == right and (numstr[left] == "6" or numstr[right] == "9"): return True
        
        return False
        
