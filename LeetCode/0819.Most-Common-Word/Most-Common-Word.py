class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        print(paragraph)        
        banned_set = set(banned)        
        words = paragraph.lower().split()
        count = collections.Counter([word for word in words if word not in banned_set])
        #print(count)
        return count.most_common(1)[0][0]
        
