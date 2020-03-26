class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        ans = []
        words = list(text.split(" ")) 
        #print words
        i = 0
        while i < len(words) - 2:
            #print words[i], first, second, words[i] == first
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])
            i += 1
        return ans
        
