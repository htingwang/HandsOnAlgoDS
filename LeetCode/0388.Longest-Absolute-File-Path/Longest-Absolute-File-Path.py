class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        path = input.split("\n")
        length = [0]
        res = 0
        for name in path:
            level = name.count("\t")
            cur = len(name) - level
            #print(name, len(name), cur)
            if level >= len(length) - 1:
                length.append(cur + length[-1])
            else:
                length[level + 1] =  cur + length[level]
            #print(length)
            if name.find(".") != -1:
                #print(name, name.find("."))
                res = max(res, length[level + 1] + level)
        return res
