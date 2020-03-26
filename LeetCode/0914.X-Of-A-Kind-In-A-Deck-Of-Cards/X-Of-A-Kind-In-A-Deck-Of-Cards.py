class Solution(object):
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b:
            a,b = b,a%b
        return a

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        exists = {};
        minsize = len(deck);
        for num in deck:
            exists[num] = exists.get(num, 0)+1;
        
        groupnum = set([]);
        for key in exists:
            groupnum.add(exists[key]);
        groupnum = list(groupnum)    
        gcdnum = groupnum[0];
        for i in range(1, len(groupnum)):
            gcdnum = self.gcd(gcdnum, groupnum[i]);
            
        return gcdnum != 1;
