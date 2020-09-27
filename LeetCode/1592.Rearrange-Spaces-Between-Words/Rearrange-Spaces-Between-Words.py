class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        if len(text) == 1: return text
        spaces = 0
        s = e = 0
        res = []
        for i, c in enumerate(text):
            if c == ' ':
                spaces += 1
            else:
                if i == 0 or text[i - 1] == ' ': s = i
                if i == len(text) - 1 or text[i + 1] == ' ':
                    res.append(text[s: i + 1])
        
        a, b = spaces // (len(res) - 1) if len(res) != 1 else 0, spaces % (len(res) - 1) if len(res) != 1 else spaces
        #print(res, spaces, a, b)
        return (" " * a).join(res) + " " * b
