from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter
