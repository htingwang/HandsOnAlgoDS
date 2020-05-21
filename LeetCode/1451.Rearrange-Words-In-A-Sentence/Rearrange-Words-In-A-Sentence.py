class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        text_list = text.split(" ")
        text_info = []
        for i in range(len(text_list)):
            text_info.append((len(text_list[i]), i))
        text_info.sort()
        res = []
        first = ""
        for i in range(len(text_list[text_info[0][1]])):
            if i == 0: first += text_list[text_info[0][1]][i].upper()
            else: first += text_list[text_info[0][1]][i]
        res.append(first)
        for i in range(1, len(text_info)):
            res.append(text_list[text_info[i][1]].lower())
        return " ".join(res)
            
        
