class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = collections.defaultdict(int)
        res = 0
        for d in dominoes:
            tmp = sorted(d)
            count[tmp[0] * 10 + tmp[1]] += 1

        for _, num in count.items():
            
            res += (num * (num - 1) / 2 )
            #print(num,res,(num * (num - 1) / 2 ))
        return res
            
        
