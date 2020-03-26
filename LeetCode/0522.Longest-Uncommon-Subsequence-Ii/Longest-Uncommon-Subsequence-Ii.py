class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort()
        strs.sort(key = len, reverse = True)
        #print(strs)
        visit = set()
        for i in range(len(strs)):
            if i == len(strs) - 1 or strs[i] != strs[i + 1]:
                found = True
                for pre in visit:
                    j = 0
                    for c in pre:
                        if c == strs[i][j]: j += 1
                        if j == len(strs[i]): break
                    if j == len(strs[i]): 
                        found = False
                        break
                if found == True: return len(strs[i])
            visit.add(strs[i])
        return -1
