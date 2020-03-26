class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        ans = []
        while label > 0:
            ans = [label] + ans
            label = label // 2
            #print(label)
        #print(ans)
        n = len(ans)
        for i in range(n):
            if i % 2 == n % 2:
                ans[i] = pow(2, i + 1) - ans[i] % pow(2, i) - 1
        #print(ans)
        return ans
