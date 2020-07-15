class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return self.hIndex2(citations)
    
    def hIndex2(self, citations):
        n = len(citations)
        papers = [0] * (n + 1)
        for c in citations:
            papers[min(n, c)] += 1

        for i in range(n, 0, -1):
            if i != n: papers[i] += papers[i + 1]
            if i <= papers[i]: return i

        return 0
        
    def hIndex1(self, citations):
        res = 0
        citations.sort(reverse = True)
        for c in citations:
            if c >= res + 1: res += 1
            else: break
        return res
