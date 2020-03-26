import collections
import bisect
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_to_pos = collections.defaultdict(list)
        for i, c in enumerate(t):
            char_to_pos[c].append(i)
        #print(char_to_pos)
        
        pivot = -1
        
        for i, c in enumerate(s):
            #if c not in char_to_pos: return False
            cur = bisect.bisect(char_to_pos[c], pivot)
            #print(cur, pivot)
            if cur == len(char_to_pos[c]): return False
            pivot = char_to_pos[c][cur]
        return True
