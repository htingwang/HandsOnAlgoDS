class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        res = []
        count = collections.defaultdict(int)
        for name in names:
            #print(name, count)
            if name not in count:
                res.append(name)
                count[name] += 1
                continue
            while count[name] > 0 and name + '(' + str(count[name]) + ')' in count:
                count[name] += 1
            res.append(name + '(' + str(count[name]) + ')')
            count[res[-1]] += 1
        return res
            
