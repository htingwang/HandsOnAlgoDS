from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        filedict = defaultdict(list)
        for path in paths:
            pathlist = path.split(" ")
            directory = pathlist[0]
            for i in range(1, len(pathlist)):
                name, content = pathlist[i].split("(")
                filedict[content].append(directory + "/" + name)
        output = []
        for content in filedict:
            if len(filedict[content]) > 1:
                output.append(filedict[content])
        return output   
