class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        m = collections.defaultdict(list)
        for word in strings:
            key = [0]
            for i in range(1, len(word)):
                key.append((ord(word[i]) - ord(word[0]) + 26) % 26)
            m[tuple(key)].append(word)
        
        res = []
        for key in m:
            res.append(m[key][:])
            
        return res
            
