import collections
class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
#s1 = "x x y y xy x yx x", 
#s2 = "x y y x yx x xy x"       
#s1 = "  x   y xy   yx  ", 
#s2 = "  y   x yx   xy  "   
        s1_to_s2 = collections.defaultdict(int)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1_to_s2[(s1[i], s2[i])] += 1
        if (s1_to_s2[("x", "y")] + s1_to_s2[("y", "x")]) % 2:
            return -1
        return s1_to_s2[("x", "y")] // 2 + s1_to_s2[("y", "x")] // 2 + 2 * (s1_to_s2[("x", "y")] % 2)
