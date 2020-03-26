class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        index = i = 0
        #print(s)
        while i < len(s):
            if s[i] != " ":
                #print(i, index)
                if index != 0:
                    s = s[:index] + " " + s[index + 1:]
                    index += 1
                    #print(s, index)
                    #i += 1
                j = i
                tmp = ""
                while j < len(s) and s[j] != " ":
                    tmp = s[j] + tmp
                    j += 1 
                #print(index, tmp, j - i)
                s = s[:index] + tmp + s[index + j - i: ]
                #print(s, i, j)
                index += (j - i)
                i = j
            else:
                i += 1
        s = s[:index]
        #print(s, index, i, j)
        return s
                
