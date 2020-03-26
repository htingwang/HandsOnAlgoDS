class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count, start = 1, 0;
        ans = [];
        for i in range(1, len(S)):
            if (S[i-1] == S[i]):
                count += 1;
            else:
                if (count >= 3):
                    ans.append([start, start+count-1]);
                count, start = 1, i;
        if (count >= 3):
            ans.append([start, start+count-1]);
        return ans;
        
