class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        i = 0
        while candies > 0:
            ans[i % num_people] += min(candies, i + 1)
            candies -= (i + 1)
            i += 1
        #print(ans)
        return ans
