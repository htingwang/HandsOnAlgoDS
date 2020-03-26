class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        G = [[] for i in range(N)];
        ans = [0] * N;
        for i, j in paths:
            G[i-1].append(j-1);
            G[j-1].append(i-1);
        #print G
        for i in range(N):
            tmp ={1, 2, 3, 4};
            for j in G[i]:
                tmp = tmp-{ans[j]};
            ans[i] = tmp.pop();
        return ans;
        
